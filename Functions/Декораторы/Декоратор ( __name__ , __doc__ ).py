# Используем wraps, чтобы сохранить первоначальные значения __name__ и __doc__

from functools import wraps


def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('</h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('</table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@decorator
def say(name, firstname):
    '''
    Print text
    :param name:
    :param firstname:
    :return:
    '''
    print(f'Hello {name} {firstname}!')


say('Vasil', 'Omchinsciy')
print(say.__name__)
print(say.__doc__)
