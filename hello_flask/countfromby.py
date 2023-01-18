class CountFromBy:
    def __init__(self, val: int = 0, incr: int = 1) -> None:
        self.val = val
        self.incr = incr

    def increase(self) -> None:
        self.val += self.incr

    def show_atr(self) -> str:
        print(f'val={self.val} incr={self.incr}')


if __name__ == '__main__':
    b = CountFromBy(50, 10)
    a = CountFromBy()
    b.increase()
    for i in range(5):
        a.increase()
    a.increase()
    b.show_atr()
    a.show_atr()
