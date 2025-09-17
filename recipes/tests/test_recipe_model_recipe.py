from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_the_test(self):
        recipe = self.recipe
        ...
        
    def test_recipe_title_raises_errors_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 66
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()