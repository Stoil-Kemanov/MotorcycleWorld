from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from accounts.forms import MotoUserCreationForm, ProfileForm
from accounts.models import MotoUser, Profile
from accounts.validators import PhoneNumberValidator


class TestProfileModel(TestCase):

    def test__profile_str_returns_username(self):
        user = MotoUser.objects.create_user(
            username='test',
            email='test@email.test',
            password='123Test456'
        )

        profile = user.profile

        self.assertEqual(str(profile), 'test')

    def test__other_user_with_same_username_raises_integrity_error(self):
        user = MotoUser.objects.create_user(
            username='test',
            email='test@email.test',
            password='123Test456'
        )

        with self.assertRaises(IntegrityError):
            user = MotoUser.objects.create_user(
                username='test',
                email='other@email.test',
                password='123Test456'
            )


class TestPhoneNumberValidator(TestCase):
    def setUp(self):
        self.validator = PhoneNumberValidator()

    def test__valid_phone_number(self):
        valid_numbers = [
            '0888123456',
            '+359 88 123 4567',
            '(088) 123-4567',
            '088-123-4567',
            '+1 (800) 123-4567',
            '',
            None
        ]

        for number in valid_numbers:
            with self.subTest(number=number):
                self.assertIsNone(self.validator(number))

    def test__invalid_phone_number(self):
        invalid_numbers = {
            '123abc456': 'Phone number can only contain digits',
            '!@#4567890': 'Phone number can only contain digits',
            '123': 'Phone number must be between 7 and 15 digits.',
            '12345678901234567890': 'Phone number must be between 7 and 15 digits.'
        }

        for number, message in invalid_numbers.items():
            with self.subTest(number=number):
                with self.assertRaises(ValidationError) as e:
                    self.validator(number)
                self.assertIn(message, str(e.exception))


class TestMotoUserCreationForm(TestCase):
    def test__save_sets_username_to_email(self):
        form_data = {
            'email': 'asda@abv.bg',
            'password1': '123Test456',
            'password2': '123Test456'
        }
        form = MotoUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'asda@abv.bg')


class TestProfileForm(TestCase):
    def test__valid_dob_format(self):
        user = MotoUser.objects.create_user(
            username='test',
            email='test@email.test',
            password='123Test456'
        )

        form = ProfileForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '+359881234567',
            'date_of_birth': '01/01/1999',
            'height': '180',
            'weight': '100',
            'body_type': 'Slim',
            'riding_style': 'Sport',
            'experience': 'Beginner (0-1 years)',
            'profile_pic': None,
        })

        form.instance.user = user

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['date_of_birth'].isoformat(), '1999-01-01')


class TestFindMyBikeView(TestCase):
    def setUp(self):
        self.user = MotoUser.objects.create_user(email='tester1@abv.bg', username='tester1', password='123Test456')
        self.client.login(email='tester1@abv.bg', password='123Test456')

    def test__redirect_if_profile_incomplete(self):
        profile = Profile.objects.get(user=self.user)
        profile.first_name = 'John'
        profile.last_name = 'Doe'
        profile.save()
        response = self.client.get(reverse('find-my-bike'))
        self.assertRedirects(response, reverse('profile-edit'))
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any('Please complete your profile first to get personalized bike recommendations!' in m.message for m in messages))

    def test__context_contains_recommendations(self):
        profile = Profile.objects.get(user=self.user)
        profile.first_name = 'John'
        profile.last_name = 'Doe'
        profile.body_type = 'Slim'
        profile.riding_style = 'Sport'
        profile.experience = 'Beginner (0-1 years)'
        profile.save()
        response = self.client.get(reverse('find-my-bike'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommendations', response.context)
        self.assertIn('profile', response.context)
        self.assertIn('get_compatibility_color', response.context)
        self.assertIn('has_recommendations', response.context)


class TestFindMyClothingView(TestCase):
    def setUp(self):
        self.user = MotoUser.objects.create_user(email='tester1@abv.bg', username='tester1', password='123Test456')
        self.client.login(email='tester1@abv.bg', password='123Test456')

    def test__redirect_if_profile_incomplete(self):
        profile = Profile.objects.get(user=self.user)
        profile.first_name = 'John'
        profile.last_name = 'Doe'
        profile.save()
        response = self.client.get(reverse('find-my-clothing'))
        self.assertRedirects(response, reverse('profile-edit'))
        messages_list = list(response.wsgi_request._messages)
        self.assertTrue(any('Please complete your profile first to get personalized clothing recommendations!' in m.message for m in messages_list))

    def test__context_contains_recommendations(self):
        profile = Profile.objects.get(user=self.user)
        profile.first_name = 'John'
        profile.last_name = 'Doe'
        profile.body_type = 'Slim'
        profile.riding_style = 'Sport'
        profile.save()
        response = self.client.get(reverse('find-my-clothing'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommendations', response.context)
        self.assertIn('profile', response.context)
        self.assertIn('get_compatibility_color', response.context)
        self.assertIn('has_recommendations', response.context)
