def num4vowels():
    """Выводит гласные и их количество найденные
     во введенном слове или фразе"""
    vowels = set('aeiouyаеёиоуэюяы')
    word = input('Введите слово или фразу на английском или русском языке'
                 ' для определения количества гласных букв: ')
    found = {}

    for letter in word:
        if letter in vowels:
            found.setdefault(letter, 0)
            found[letter] += 1

    if not found:
        print('Гласных букв не обнаружено.')
    else:
        for k, v in sorted(found.items()):
            print('Гласная ', k, 'найдена ', v, 'раз.')


if __name__ == '__main__':
    num4vowels()
