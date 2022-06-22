# ООП 2.11 - Stepik

from string import digits, ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(new_password):
        for digit in digits:
            if digit in new_password:
                return True
        return False

    @staticmethod
    def is_include_all_register(new_password):
        flag_upper = False
        flag_lower = False
        for letter in new_password:
            if letter.isupper():
                flag_upper = True
            if letter.islower():
                flag_lower = True
        if flag_lower and flag_upper:
            return True
        return False

    @staticmethod
    def is_include_only_latin(new_password):
        for letter in new_password:
            if letter not in ascii_letters and letter.isalpha():
                return False
        return True

    @staticmethod
    def check_password_dictionary(new_password):
        with open('easy_passwords.txt') as p:
            for easy_password in p.readlines():
                if new_password == easy_password.strip():
                    return False
        return True

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 11 >= len(new_password) >= 4:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(new_password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(new_password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(new_password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(new_password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = new_password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if new_login.count('@') != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' not in new_login[new_login.find('@'):] or not new_login[new_login.find('@'):].count('.') == 1:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124
r1.password = 'yyyt12tttRF'
print(r1.login, r1.password)
