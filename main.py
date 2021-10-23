
def equation(a=1234564678, b=2, x=3, c=1851847015):
    return a / b * x - c

def arithmtic(a, b, c):
    if b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    elif b == '/':
        print(a / c)
    elif b == '*':
        print(a * c)
    else:
        print('Unknown operation')

def is_year_leap(year):
    if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        print('високосный год')
    elif year % 4 != 0 and year % 100 != 0 or year % 400 != 0:
        print('невисикосный год')
    else:
        print('unknown operation')

def square(a):
    p = a + a + a + a
    s = a * a
    d = a ** 0.5
    sqr = (p, s, d)
    return sqr

def season(month):
    if month == int and month == 3 or month < 6:
        print('Весна')
    elif month == 6 or month < 9:
        print('Лето')
    elif month == 9 or month < 12:
        print('Осень')
    elif month == 12 or month < 3:
        print('Зима')
    else:
        print('Ошибка')

def bank(years = 2019, money = 20000):
    next_years = years + 1
    persents = money * 0.1
    next_years_persents = money + persents
    if years == 2019:
        print(money)
    elif next_years > 2019:
        print(next_years_persents)
    else:
        return


if __name__ == '__main__':
    print(equation())

    print(arithmtic(4, '+', 2))
    print(arithmtic(4, '-', 2))
    print(arithmtic(4, '/', 2))
    print(arithmtic(4, '*', 2))
    print(arithmtic(4, '=', 2))

    print(is_year_leap(366))
    print(square(4))
    print(season(3))
    print(bank(2013, 20000))
    print(bank(2019, 20000))


