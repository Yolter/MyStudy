my_list = list(range(0, 10))
my_back_list = list(range(10, 0, -1))
fruits = ['банан', 'Яблоко', 'апельсин', 'Киви']


def sort(i):
    return abs(i - 5)


if __name__ == '__main__':
    # print(my_list)
    # my_list[1:len(my_list)] = 7, 8
    # my_list.insert(0, 1)
    # my_list.append(10)
    # my_list.extend(range(10, 15))
    # my_list.remove(0)
    # my_list.remove(0)
    # zero = my_list.pop(0)
    # print(zero)
    # del my_list[0]
    # my_list.clear()

    # for i in range(len(my_list)):
    #     print(my_list[i])

    # i = 0
    # while i < len(my_list):
    #     print(my_list[i])
    #     i += 1

    # [print(i) for i in my_list]

    # print(my_list)

    # print(my_back_list)
    # my_back_list.sort()
    # print(my_back_list)
    #
    # print(fruits)
    # fruits.sort()
    # print(fruits)
    # fruits.sort(key=str.lower)
    # print(fruits)

    # print(fruits)
    # fruits.reverse()
    # print(fruits)

    # print(my_list)
    # my_list.sort(reverse=True)
    # print(my_list)

    print(my_list)
    my_list.sort(key=sort)
    print(my_list)
