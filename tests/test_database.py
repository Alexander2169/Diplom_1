import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from ingredient_types import *

class TestDatabase:
    @pytest.fixture
    def database(self):
        """Создает экземпляр базы данных для тестов."""
        return Database()

    def test_available_buns(self, database):
        """Проверяет, что метод available_buns возвращает правильные булочки."""
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_price() == 200
        assert buns[2].get_price() == 300

    def test_available_ingredients(self, database):
        """Проверяет, что метод available_ingredients возвращает правильные ингредиенты."""
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

    def test_bun_initialization(self):
        """Проверяет, что булочки инициализируются с правильными значениями."""
        bun = Bun("test bun", 150)
        assert bun.get_name() == "test bun"
        assert bun.get_price() == 150

    def test_ingredient_initialization(self):
        """Проверяет, что ингредиенты инициализируются с правильными значениями."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)
        assert ingredient.get_name() == "test sauce"
        assert ingredient.get_price() == 50
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_database_initialization(self):
        """Проверяет, что база данных инициализируется с правильными булочками и ингредиентами."""
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

        # Проверяем булочки
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[1].get_name() == "white bun"
        assert database.buns[2].get_name() == "red bun"

        # Проверяем ингредиенты
        assert database.ingredients[0].get_name() == "hot sauce"
        assert database.ingredients[1].get_name() == "sour cream"
        assert database.ingredients[2].get_name() == "chili sauce"
        assert database.ingredients[3].get_name() == "cutlet"
        assert database.ingredients[4].get_name() == "dinosaur"
        assert database.ingredients[5].get_name() == "sausage"
