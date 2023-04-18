# import time
from pprint import pprint

# start = time.time()
squares = [i * i for i in range(20)]

even_squares = [y for i in range(20) if (y := i * i) % 2 == 0 and y > 0]
# end = time.time()

text = 'ЧтО - Такое ЛеТо'

new_text = ''.join([letter.lower() for letter in text])

# translit = {'ч': 'ch', 'т': 't', 'а': 'a', 'к': 'k'}

new_text2 = ' '.join(
    [letter for letter in text.split() if letter != '-']
).capitalize()

ints = [-1, -2, -3, 7, 3, 2, 0]

positives = [i for i in ints if i > 0]

matrix = [list(range(i, i + 3)) for i in range(3)]

if __name__ == '__main__':
    print(f'squares: {squares}')
    print(f'even_squares: {even_squares}')
    print(f'text: {text}')
    print(f'new_text: {new_text}')
    print(f'new_text2: {new_text2}')
    print(f'ints: {ints}')
    print(f'positives: {positives}')
    pprint(matrix, width=20)
