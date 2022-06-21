# ООП 2.11 - Stepik

from string import digits


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.__secret_word = 'NICE'

    @property
    def secret_words(self):
        ss = input('Введите пароль: ')
        if ss == self.password:
            return self.__secret_word
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def easy_password(password):
        with open('passwords.txt') as s:
            for i in s.readlines():
                if password == i.strip():
                    return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 6:
            raise ValueError('Пароль должен быть больше 5 символов')
        if len(value) > 15:
            raise ValueError('Пароль должен быть меньше 15 символов')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if User.easy_password(value):
            raise ValueError('Пароль слишком легкий')
        self.__password = value

u1 = User('fas','asfdg4grfa')
print(u1.password)
u1.password = '123456wef'
print(u1.password)
print(u1.secret_words)