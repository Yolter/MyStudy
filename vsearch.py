def search4vowels():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = input('Введите английское слово или фразу для определения гласных букв: ')
    vowels_in_word = vowels.intersection(set(word))
    for i in vowels_in_word:
        print(i)
