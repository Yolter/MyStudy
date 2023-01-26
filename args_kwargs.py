def myfunc(*args):
    for _ in args:
        print(_, sep='->', end=' ')
    print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    print()


if __name__ == '__main__':
    val_1 = [1, 2, 3]
    val_2 = [4, 5, 6]
    num = {'one': 1, 'two': 2, 'three': 3}

    myfunc(1, 2, 'три')
    myfunc(*val_1, val_2)
    myfunc2(one=1, two=2)
    myfunc2(**num)
