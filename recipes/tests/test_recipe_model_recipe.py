from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
        category=self.make_category(name='new category'),
        author=self.make_author(username='newuser2'),
        title='recipe title',
        description= 'recipe description',
        slug= 'recipe-title',
        preparation_time= 10,
        preparation_time_unit= 'minutos',
        servings= 4,
        servings_unit= 'pessoas', 
        preparation_steps= 'teste', 
        )
        recipe.full_clean()
        recipe.save()
        return recipe
        
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])      
    def test_recipe_fields_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
            
    def test_recipe_preparation_steps_is_html_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html)
    
    def test_recipe_is_published_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published)
        
    def test_recipe_string_representation(self):
        recipe_title_test = 'Testing Recipe Title'
        self.recipe.title = 'Testing Recipe Title'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), recipe_title_test
        )    
