import threading
from time import sleep

res = []
class Knight(threading.Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
         count = 0
         res.append(f'{self.name}, на нас напали!')

         while self.enemies > 0:
             count += 1
             self.enemies -= self.power
             if self.enemies < 0:
                 self.enemies = 0
             res.append(f'{self.name}, сражается {count} день(дня)..., осталось {self.enemies} войнов.')
             sleep(1)

             res.append(f'{self.name} одержал победу спустя {count} дней(дня)')

if __name__ == '__main__':

    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    for text in res:
        print(text)

    print('Все битвы закончились!')

