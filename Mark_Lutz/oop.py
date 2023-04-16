from accessify import *


class Point:
    color = 'red'
    circle = 2
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def set_limit(cls, min_coord: (int, float), max_coord: (int, float)):
        cls.MIN_COORD = min_coord
        cls.MAX_COORD = max_coord

    @private
    @classmethod
    def validate(cls, arg: (int, float)) -> bool:
        return type(arg) in (int, float) \
            and cls.MAX_COORD >= arg >= cls.MIN_COORD

    # метод __new__ вызывается при моздании нового экземпляра класса,
    # используется для реализации паттерна Singleton
    def __new__(cls, *args, **kwargs):
        print(f'Оппа па! создается новый объект класса {str(cls)}')
        # если переопределяем метод __new__,
        # без этой строки новый объект не будет создан!
        return super().__new__(cls)

    def __init__(self, x: int = 0, y: int = 0, lock: int = 0):
        self.__x = self.__y = self.lock = 0
        if self.validate(x) and self.validate(y) and self.validate(lock):
            self.__x = x
            self.__y = y
            self.lock = lock
        else:
            raise ValueError(
                'Значения атрибутов x и y не попадают в диапазон от 0 до 100, либо не являются числами')

    # метод __del__ вызывается при удалении экземпляра класса
    def __del__(self):
        print(f'Ой!, кажется удалили объект {str(self)}')

    def set_attr(self, x: int, y: int) -> None:
        if self.validate(x) and self.validate(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError(
                'Значения атрибутов x и y не попадают в диапазон от 0 до 100, либо не являются числами')

    def get_attr(self) -> None:
        print(f'Атрибут Х={self.__x}, атрибут У={self.__y}')

    # метод __getattribute__ вызывается при обращении к атрибуту
    # экземпляра класса
    def __getattribute__(self, item):
        if item == 'lock':
            # генерация исключения raise ValueError() запрещает доступ
            # к атрубуту "у" даже через метод, например: get_attr()
            raise ValueError('Доступ к атрибуту "lock" запрещен')
        else:
            return object.__getattribute__(self, item)

    # метод __setattr__ вызывается при присвоении значения атрибуту
    # экземпляра класса
    def __setattr__(self, key, value):
        # может использоваться, например, для запрещения создания атрибута с
        # определенным именем
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

    # метод __getattr__ вызывается при обращении к несуществующему атрибуту
    # экземпляра класса
    def __getattr__(self, item):
        # может использоваться для замены вывода ошибки на что-то другое,
        # например, 'False'
        return False

    # метод __delattr__ вызывается при удалении атрибута экземпляра класса
    def __delattr__(self, item):
        print('удален атрибут: ' + item)
        object.__delattr__(self, item)


# паттерн "моносостояние" позволят создавать новые экземпляры класса
# с одинаковыми атрибутами
class Mono:
    __shared_data = {
        'name': 'user',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_data




class Person:
    def __init__(self, name: str, old: int):
        self.__name = name
        self.__old = old

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


if __name__ == '__main__':
    # pt = Point(1, 12, 50)
    # pt.set_attr(23, 45)
    # pt.get_attr()
    # pt.b = 123
    # print(pt.__dict__)
    # del pt.b
    # print(pt.__dict__)

    # mn1 = Mono()
    # mn1.__dict__['name'] = 'vlad'
    # mn2 = Mono()
    # print(mn1.__dict__)
    # print(mn2.__dict__)

    guy = Person('Nick', 31)
    print(guy.name)
    guy.name = 'Vlad'
    print(guy.__dict__)
