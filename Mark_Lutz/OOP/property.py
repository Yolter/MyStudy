from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, old: int, ps: int, weight: float):
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

    @classmethod
    def verify_old(cls, old):
        if old in int and 120 >= old >= 14:
            return old
        else:
            raise ValueError(
                'Возвраст должен быть числом в диапазоне от 14 до 120 лет')

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    # свойства property позволяют обращаться к сеттерам и геттерам
    # через единый интерфейс экземпляра класса property
    old = property(get_old, set_old)

    # однако, на практике используют декоратор @property, чтобы избежать
    # функционального дублирования
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name
