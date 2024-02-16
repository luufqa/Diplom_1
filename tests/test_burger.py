from bun import Bun
from data.data import Buns
from burger import Burger
from ingredient import Ingredient
from ingredient_types import IngredientTypes


class TestBurger:

    def test_set_buns(self):
        buns = Buns()
        burger = Burger()
        burger.set_buns(buns.cosmos_bun)
        assert burger.bun == buns.cosmos_bun

    def test_add_move_del_ingredient(self):
        burger = Burger()
        burger.add_ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE)
        burger.add_ingredient(IngredientTypes.INGREDIENT_TYPE_FILLING)
        burger.move_ingredient(0, 1)
        burger.remove_ingredient(1)
        assert burger.ingredients == [IngredientTypes.INGREDIENT_TYPE_FILLING]

    def test_get_price(self):
        buns = Buns()
        burger = Burger()
        burger.add_ingredient(Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, 'Томатный', 13))
        burger.set_buns(Bun(buns.black_bun, buns.black_bun_price))
        result = burger.get_price()
        assert result == 37.4

    def test_get_receipt(self):
        buns = Buns()
        burger = Burger()
        burger.add_ingredient(Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, 'Томатный', 13))
        burger.set_buns(Bun(buns.black_bun, buns.black_bun_price))
        result = burger.get_receipt()
        assert "Price: 37.4" in result
