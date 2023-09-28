import csv
import os.path


#from src.csv_errors import InstantiateCSVError
class Item:
    """
    Класс для представления товара в магазине.
    """
    self = None
    pay_rate = 1.0
    all = []
    name_len = 10
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self.name


    @property
    def name(self):
        """Геттер для атрибута name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Сеттер для name, с проверкой длины наименования товара"""
        if len(name) <= self.name_len:
            self.__name = name
        else:
            self.__name = name[:self.name_len]

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """класс-метод, инициализирующий экземпляры класса `Item` данными
         из файла _src/items.csv_"""

        with open(file_name, encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price


    def add_attribute(self) -> None:
        self.quantity = self.quantity + Phone.self.quantity
        return self.quantity

    def __add__(self, other):
        """
    	Метод срабатывает, когда используется оператор сложения.
    	В параметре other хранится то, что справа от знака +
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Операция сложения не доступна для экземпляров класса.")



