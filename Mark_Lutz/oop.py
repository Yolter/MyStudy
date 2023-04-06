from accessify import *


class Point:
    color = 'red'
    circle = 2
    MIN_COORD = 0
    MAX_COORD = 100

    @private
    @classmethod
    def validate(cls, arg: (int, float)) -> bool:
        return type(arg) in (int, float) \
            and cls.MAX_COORD >= arg >= cls.MIN_COORD

    def __new__(cls, *args, **kwargs):
        print(f'Оппа па! создается новый объект класса {str(cls)}')
        # если переопределяем метод __new__,
        # без этой строки новый объект не будет создан!
        return super().__new__(cls)

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = self.__y = 0
        if self.validate(x) and self.validate(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError(
                'Значения атрибутов x и y не попадают в диапазон от 0 до 100, либо не являются числами')

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


if __name__ == '__main__':
    pt = Point(1, 12)
    pt.get_attr()
    pt.set_attr(23, 45)
    pt.get_attr()

