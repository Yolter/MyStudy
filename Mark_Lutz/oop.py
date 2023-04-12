from accessify import *

# test
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

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.__x = x
            self.y = y
        else:
            raise ValueError(
                'Значения атрибутов x и y не попадают в диапазон от 0 до 100, либо не являются числами')

    # метод __del__ вызывается при удалении экземпляра класса
    def __del__(self):
        print(f'Ой!, кажется удалили объект {str(self)}')

    def set_attr(self, x: int, y: int) -> None:
        if self.validate(x) and self.validate(y):
            self.__x = x
            self.y = y
        else:
            raise ValueError(
                'Значения атрибутов x и y не попадают в диапазон от 0 до 100, либо не являются числами')

    def get_attr(self) -> None:
        print(f'Атрибут Х={self.__x}, атрибут У={self.y}')

    # метод __getattribute__ вызывается при обращении к атрибуту экземпляра класса
    def __getattribute__(self, item):
        if item == 'y':
            print('К атрибуту "y" доступ запрещен!')
            return object.__getattribute__(self, item)
            # генерация исключения raise ValueError() запрещает доступ
            # к атрубуту "у" даже через метод, например: get_attr()
        else:
            return object.__getattribute__(self, item)

    # метод __setattr__ вызывается при присвоении значения атрибуту
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
#       # например, 'False'
        return False

if __name__ == '__main__':
    pt = Point(1, 12)
    pt.set_attr(23, 45)
    # pt.get_attr()
    print(pt.aa)


