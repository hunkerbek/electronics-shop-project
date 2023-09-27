

class Phone:
    """ Класс для представления товара в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """Создание экземляра класса Phone

        :param name: Название товара.
        :param price: Цена за еденицу товара.
        :param quantity: Колличество товара в магазине.
        :param number_of_sim: Колличество поддерживаемых сим-карт
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

    #def __repr__(self):
    #    return f"{self.__class__.__name__},('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name


    def __add__(self, other):
        """
    	Метод срабатывает, когда используется оператор сложения.
    	В параметре other хранится то, что справа от знака +
        """
        return self.quantity + other.quantity


    def __add__(self, other):
        """
    	Метод срабатывает, когда используется оператор сложения.
    	В параметре other хранится то, что справа от знака +
        """
        return self.number_of_sim + other.number_of_sim