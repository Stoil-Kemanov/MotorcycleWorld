from django.test import TestCase

from clothing.models import Clothing


class TestClothingModel(TestCase):

    def test__clothing_str_returns_make_model_category(self):
        clothing = Clothing.objects.create(
            make="Dainese",
            model="Super",
            category="Jacket",
            fit="Slim",
            style="Sport",
            price="100.00"
        )

        self.assertEqual(str(clothing), "Dainese Super Jacket")

