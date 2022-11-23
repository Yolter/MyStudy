vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё',
          'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
word = input('Введите слово или фразу на английском или русском языке'
             ' для определения количества гласных букв: ')
found = {}

for letter in word:
    if letter in vowels:
        if letter not in list(found.keys()):
            found[letter] = 1
        else:
            found[letter] += 1

for k, v in sorted(found.items()):
    print('Гласная ', k, 'найдена ', v, 'раз')
