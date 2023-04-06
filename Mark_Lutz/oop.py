class Point:
    color = 'red'
    circle = 2

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_attr(self):
        print(f'Атрибут Х={self.x}, атрибут У={self.y}')


if __name__ == '__main__':
    pt1 = Point(10, 20)
    pt1.get_attr()
