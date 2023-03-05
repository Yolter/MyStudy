phrase = list(input('Введите слово или фразу, а я проверю, пaлиндром ли это: '))

back_phrase = []

for i in phrase:
    if i == ' ':
        phrase.remove(' ')

back_phrase = phrase[::-1]

if phrase == back_phrase:
    print('Это палиндром')
else:
    print('Это не палиндром')
