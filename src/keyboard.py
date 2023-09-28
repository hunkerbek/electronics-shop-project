from src.item import Item

class Mixin:

    @property
    def language(self):
        return self._language[self._language_id]

    def change_lang(self):
        self._language_id += 1
        if self._language_id >= len(self._language):
            self._language_id = 0


class Keyboard(Item, Mixin):
    name_len = 20
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language_id = 0
        self._language = ["EN", "RU"]
