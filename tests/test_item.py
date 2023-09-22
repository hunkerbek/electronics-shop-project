"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 20000, 20)
    item2 = Item("Ноутбук", 10000, 5)

    assert (item1.calculate_total_price()) == 400000
    assert (item2.calculate_total_price()) == 50000


def test_apply_discount():
    item1 = Item("Смартфон", 20000, 20)
    item2 = Item("Ноутбук", 10000, 5)

    Item.pay_rate = 0.8

    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 16000.0
    assert item2.price == 8000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_name_prop():
    item1 = Item("",0,0)
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"
    item1.name = "СмартфонСмартфон"
    assert item1.name == "СмартфонСм"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'