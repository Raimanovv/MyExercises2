def decorator(func):
    def inner(*args, **kwargs):
        print('</h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('</table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

@decorator
@table
def say(name, firstname):
    print(f'Hello {name} {firstname}!')


say('Vasil', 'Omchinsciy')
