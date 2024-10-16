import pytest
from unittest.mock import Mock
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Булочка 1", 50.0),
        ("Булочка 2", 75.5),
        ("Булочка 3", 100.0),
    ])
    def test_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_get_name(self):
        bun = Bun("Булочка", 30.0)
        assert bun.get_name() == "Булочка"

    def test_get_price(self):
        bun = Bun("Булочка", 30.0)
        assert bun.get_price() == 30.0

    def test_price_type(self):
        bun = Bun("Булочка", 30.0)
        assert (bun.get_price(), float)

    def test_name_type(self):
        bun = Bun("Булочка", 30.0)
        assert (bun.get_name(), str)

    def test_bun_with_mock(self):
        # Создаем мок для класса Bun
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Сдобная булочка"
        mock_bun.get_price.return_value = 25.0

        assert mock_bun.get_name() == "Сдобная булочка"
        assert mock_bun.get_price() == 25.0

