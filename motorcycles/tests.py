from django.test import TestCase

from motorcycles.forms import UniversalSearchForm


class TestUniversalSearch(TestCase):
    def test__search_valid_form(self):
        form = UniversalSearchForm(data={'search': 'Honda'})
        self.assertTrue(form.is_valid())

    def test__invalid_min_price_form(self):
        form = UniversalSearchForm(data={'min_price': 'e'})
        self.assertFalse(form.is_valid())
        self.assertIn('min_price', form.errors)
