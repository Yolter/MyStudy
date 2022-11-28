word = 'бутылок'

for number_of_bottle in range(99, 0, -1):
    print(number_of_bottle, word, 'пива на стене')
    print(number_of_bottle, word, 'пива')
    print('Возьми одну, пусти по кругу')
    if number_of_bottle == 1:
        word = 'бутылок'
        print('Нет', word, 'пива на стене')
        print()
        print('Нет', word, 'пива на стене')
        print('Нет', word, 'пива')
        print('Пойди в магазин и купи еще')
        print(99, word, 'пива на стене')
    else:
        new_number_of_bottle = number_of_bottle - 1
        if 11 <= new_number_of_bottle <= 14:
            word = 'бутылок'
        elif new_number_of_bottle % 10 in [2, 3, 4]:
            word = 'бутылки'
        elif new_number_of_bottle % 10 == 1:
            word = 'бутылка'
        else:
            word = 'бутылок'
        print(new_number_of_bottle, word, 'пива на стене')
        print()