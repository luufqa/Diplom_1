from bun import Bun
from data.data import Buns
import pytest


class TestBun:

    @pytest.mark.parametrize("bun, price", [
        (Buns.cosmos_bun, Buns.cosmos_bun_price),
        (Buns.black_bun, Buns.black_bun_price)
    ])
    def test_get_name_bun(self, bun, price):
        buns = Bun(bun, price)
        result = buns.get_name()
        assert result == bun

    @pytest.mark.parametrize("bun, price", [
        (Buns.cosmos_bun, Buns.cosmos_bun_price),
        (Buns.black_bun, Buns.black_bun_price)
    ])
    def test_get_price_bun(self, bun, price):
        buns = Bun(bun, price)
        result = buns.get_price()
        assert result == price
