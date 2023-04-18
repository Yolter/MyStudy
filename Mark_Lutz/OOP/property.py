from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self,
                 fio: str,
                 old: int,
                 ps: str,
                 weight: (float, int)
                 ) -> None:
        # при создании интерфейса взаимодействия с атрибутами через декоратор
        # @property, лучше не дублировать проверки, так как при инициализации
        # атрибутов стоит их назначать через созданные интерфейсы
        # self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_ps(ps)
        # self.verify_weight(weight)

        # те вместо __fio указываем fio и Python, согласно приоритету,
        # будет обращаться к соответствующему сеттеру
        self.fio = fio
        self.old = old
        self.ps = ps
        self.weight = float(weight)

    @classmethod
    def verify_fio(cls, fio: str):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old: int):
        if type(old) != int:
            raise TypeError('Возраст должен быть целым числом')
        if old < 14:
            raise TypeError('Вы еще очень молоды :)')
        if old > 120:
            raise TypeError('Делитесь эликсиром бессмертия ;)')

    @classmethod
    def verify_ps(cls, ps: str):
        if type(ps) != str:
            raise TypeError('Паспортные данные должны быть строкой')
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Паспортные данные должны быть в формате "**** ******"')
        for n in s:
            if not n.isdigit():
                raise TypeError('Паспортные данные должны содержать только целые числа')

    @classmethod
    def verify_weight(cls, weight: (float, int)):
        if weight < 20:
            raise TypeError('Вес слишком мал, мы очень переживаем за вас :(')

    def get_old(self) -> int:
        return self.__old

    def set_old(self, old: int):
        self.verify_old(old)

        self.__old = old

    def del_old(self):
        del self.__old

    # свойства property позволяют обращаться к сеттерам и геттерам
    # через единый интерфейс экземпляра класса property
    old = property(get_old, set_old, del_old)

    # однако, на практике используют декоратор @property, чтобы избежать
    # функционального дублирования
    # т.е. (несколько интерфейсов для однотипного взаимодействия с атрибутами)
    @property
    def fio(self) -> str:
        return self.__fio

    @fio.setter
    def fio(self, fio: str):
        self.verify_fio(fio)

        self.__fio = fio

    @fio.deleter
    def fio(self):
        del self.__fio

    @property
    def ps(self) -> str:
        return self.__passport

    @ps.setter
    def ps(self, ps: str):
        self.verify_ps(ps)
        self.__passport = ps

    @ps.deleter
    def ps(self):
        del self.__passport

    @property
    def weight(self) -> (int, float):
        return self.__weight

    @weight.setter
    def weight(self, weight: (int, float)):
        self.verify_weight(weight)
        self.__weight = weight

    @weight.deleter
    def weight(self):
        del self.__weight


if __name__ == '__main__':
    Ivan = Person('Пригульнов Иван Андреевич', 30, '1234 567897', 100)
    Ivan.ps = '9874 654123'
    print(Ivan.__dict__)
