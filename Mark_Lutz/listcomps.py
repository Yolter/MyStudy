# import time

# start = time.time()
squares = [i * i for i in range(20)]

even_squares = [y for i in range(1000) if (y := i * i) >= 100]
# end = time.time()

word = 'Что - Такое'

new_word = ''.join(
    [letter.lower() for letter in word]
)

if __name__ == '__main__':
    print(new_word)
