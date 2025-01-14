from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        if len(self.words) > 0:
            return choice(self.words)
        else:
            return ''

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for element in data_set:
                f.write(f'{element}\n')
    return write_everything

def main():
    # запишем переменные строковые:
    first = 'Кошка пела песню'
    second = 'Мошка летала быстро'

    print(list(map(lambda x, y: x==y, first, second)))

    # здесь запишем строку примера:
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    # Здесь обратимся к созданному классу мистикбол:
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())

if __name__ == '__main__':
    main()