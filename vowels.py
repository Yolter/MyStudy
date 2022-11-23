vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё',
          'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
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
