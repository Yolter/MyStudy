import math
def ceil_func():
    for i in range(20):
        p = 10 ** -i + 3
        print(f'значение i: {p}, значение округления: {math.ceil(p)}')
        if math.ceil(p) == 3:
            break


name = 'Ivan'
age = 34
def myfunc():
    global name
    name = 'Oleg'
    global age
    age = 12
    print(f"My name is {name}, i'm {age} years old")

def format_func():
    text = 'My Dear friend,\n my name is {1}, i\'m {0} years old.'
    name = 'Ivan'
    age = 34
    print(text.format(age, name))


if __name__ == '__main__':
    myfunc()
    print(name, age)
    format_func()