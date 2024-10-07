import math
def add_everything_up(a, b):
    try:
        result = round((a + b), 3)  # здесь округляем до 3 знаков после запятой
    except TypeError:
        result = str(a) + str(b)
    return result

def main():
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

if __name__ == '__main__':
    main()