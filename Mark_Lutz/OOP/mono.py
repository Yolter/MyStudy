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


if __name__ == '__main__':
    mn1 = Mono()
    mn1.__dict__['name'] = 'vlad'
    mn2 = Mono()
    print(mn1.__dict__)
    print(mn2.__dict__)