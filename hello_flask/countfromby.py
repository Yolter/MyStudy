class CountFromBy:
    def __init__(self, val: int = 0, incr: int = 1) -> None:
        self.val = val
        self.incr = incr
        print(f'Значение объекта: {self.val}')
        print(f'Шаг увеличения: {self.incr}')

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val) + ' ' + str(self.incr)


if __name__ == '__main__':
    b = CountFromBy(50, 10)
    a = CountFromBy()
    b.increase()
    for i in range(5):
        a.increase()
    a.increase()
    print(b)
