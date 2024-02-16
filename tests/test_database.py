from unittest.mock import patch
from database import Database


class TestDatabase:
    def test_database_buns(self):
        db = Database()
        available_buns = db.available_buns()
        asd = []
        for bun in available_buns:
            asd.append([bun.name, bun.price])
        print(asd)
        assert len(asd) == 3

    def test_database_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()
        asd = []
        for ingredients in available_ingredients:
            asd.append([ingredients.type, ingredients.name, ingredients.price])
        assert len(asd) == 6

    @patch('database.Database.available_buns')
    def test_database_use_mock(self, mock_available_buns):
        mock_available_buns.return_value = [['black bun', 100], ['white bun', 200], ['red bun', 300]]
        db = Database()
        assert len(db.available_buns()) == 3