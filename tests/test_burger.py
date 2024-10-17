import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:
    @pytest.fixture  # Mок для класса Bun, который возвращает имя и цену булочки
    def bun_mock(self):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Булочка"
        bun.get_price.return_value = 50.0
        return bun

    @pytest.fixture  # Mок для класса Ingredient, который возвращает имя, цену и тип ингредиента
    def ingredient_mock(self):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "помидор"
        ingredient.get_price.return_value = 10.0
        ingredient.get_type.return_value = "начинка"
        return ingredient

    def test_set_buns(self, bun_mock):  # Проверяем, что метод set_buns устанавливает булочку
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):  # Проверяем, что метод add_ingredient добавляет ингредиен
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient(self, ingredient_mock): # Проверяем, что метод remove_ingredient удаляет ингредиент
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, ingredient_mock): # Проверяем, что метод move_ingredient перемещает ингредиент
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_mock)  # Добавляем еще один ингредиент
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient_mock
        assert burger.ingredients[0] == ingredient_mock

    def test_get_price(self, bun_mock, ingredient_mock): # Проверяем, что метод get_price возвращает правильную цену
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 110.0  # 50 (булочка) * 2 + 10 (ингредиент)

    def test_get_receipt(self, bun_mock, ingredient_mock): # Проверяем, что метод get_receipt возвращает правильный чек
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_receipt = (
            '(==== Булочка ====)\n'
            '= начинка помидор =\n'
            '(==== Булочка ====)\n'
            'Price: 110.0'
        )
        assert burger.get_receipt() == expected_receipt
