try:
    with open('myfile.txt', 'w') as data:
        print(input('Введите фразу: '), file=data)
    with open('myfile.txt') as data:
        data_file = data.read()
    print(data_file)
# except NameError:
#     print('File not found.')
# except io.UnsupportedOperation:
#     print('File not writable')
except Exception as err:
    print(err)
