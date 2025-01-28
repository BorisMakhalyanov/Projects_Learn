import queue
import threading
from time import sleep
import random

class Table:
    """Класс Table: представляет стол в кафе."""
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    """Класс Guest: представляет гостя, который сидит за столом."""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Имитация времени, которое гость проводит за столом
        sleep(random.randint(3, 10))


class Cafe:
    """Класс Cafe: представляет кафе с несколькими столами и очередью гостей."""
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:  # Стол свободен
                    guest.start()  # Запускаем поток для гостя
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:  # Все столы заняты
                self.queue.put(guest)
                print(f'{guest.name} ждет в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} поел(-а) и ушел(-а)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')

                if not self.queue.empty() and table.guest is None:
                    guest = self.queue.get()
                    guest.start()
                    table.guest = guest
                    print(f'{guest.name} из очереди сел(-а) за стол номер {table.number}')


# Создаем столы
tables = [Table(number) for number in range(1, 6)]

# Список имен гостей
guests_names = ['Мария', 'Олег', 'Вахтанг', 'Сергей', 'Дарья', 'Арман', 'Виктория', 'Никита', 'Галина',
                'Павел', 'Илья', 'Александра']

# Создаем гостей
guests = [Guest(name) for name in guests_names]

# Создаем кафе и запускаем симуляцию
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
