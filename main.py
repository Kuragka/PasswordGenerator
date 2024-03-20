import random

YeS = ['д', 'Д', 'y', 'Y', 'Yes', 'Да', 'да', 'lf', 'LF']
digits = '0123456789'
lowercase_abc = 'abcdefghijklmnopqrstuvwxyz'
uppercase_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def password_generate(count, leng, text):
    abc = [i for i in text]
    for _ in range(count):
        random.shuffle(abc)
        new_abc = abc[0:leng]
        print('Ваш пароль:', *new_abc, sep='')


while True:
    answ = input('На следующие вопросы отвечай цифрами, понял? да - 1, нет - фыв')
    if answ != '1':
        print('Я разве не по русски написал?')
        continue
    else:
        n = int(input('Количество паролей для генерации: '))
        lenght = int(input('Введите длину пароля: '))
        break

while True:
    chars = ''
    answ1 = input('На следующие вопросы отвечай буквами, понял? да - да, нет - 123')
    if answ1 in YeS:
        pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
        if pwd_digits in YeS:
            chars += digits
        pwd_uppercase = input('Включать ли в пароль заглавные буквы? ')
        if pwd_uppercase in YeS:
            chars += uppercase_abc
        pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
        if pwd_lowercase in YeS:
            chars += lowercase_abc
        pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
        if pwd_punctuation in YeS:
            chars += punctuation
        password_generate(n, lenght, chars)
        break
    else:
        print('Я разве не по русски написал?')
        continue
