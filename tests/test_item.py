"""Здесь надо написать тесты с использованием pytest для модуля item."""

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

    #assert(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
