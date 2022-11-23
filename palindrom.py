phrase = input('Введите слово или фразу, а я проверю, пaлиндром ли это: ')
l_phrase = list(phrase)
back_phrase = []

for i in l_phrase:
    if i == ' ':
        l_phrase.remove(' ')

back_phrase = l_phrase[::-1]

if l_phrase == back_phrase:
    print('Это палиндром')
else:
    print('Это не палиндром')
