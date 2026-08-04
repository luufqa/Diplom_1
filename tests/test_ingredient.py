from ingredient import Ingredient
from ingredient_types import IngredientTypes
import pytest


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (IngredientTypes.INGREDIENT_TYPE_SAUCE, 'Томатный', 40),
        (IngredientTypes.INGREDIENT_TYPE_FILLING, 'Сырный', 45.0)
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type
