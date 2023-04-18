my_tuple = ('one', 'one', 'three')
add = ('four',)

if __name__ == '__main__':
    print(my_tuple)
    my_tuple += add
    print(my_tuple)
    (a, b, *c) = my_tuple  # unpacking tuple
    print(a, b, c, sep=' || ')
    print(my_tuple.count('one'))
    print(my_tuple.index('four'))