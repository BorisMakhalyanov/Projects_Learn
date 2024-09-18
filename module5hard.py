import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.Password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title
    def __eq__(self, other):
        return self.title == other

class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None
    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[self.users.index(nickname)].password == hash(password):
                self.current_user = self.users[self.users.index(nickname)]
            else:
                print('Пароль не верен.')
        else:
            print(f"Пользователь {nickname} не существует")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.current_user = user
    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, title):
        video_list = []
        for video in self.videos:
            if video.title.lower().find(title.lower()) != -1:
                video_list.append(video.title)
        return video_list

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif title in self.videos:
            title_number = self.videos.index(title)
            if self.videos[title_number].adult_mode is True and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                while self.videos[title_number].time_now < self.videos[title_number].duration:
                    time.sleep(1)
                    self.videos[title_number].time_now += 1
                    print(self.videos[title_number].time_now, end=' ')
                self.videos[title_number].time_now = 0
                print("Конец видео")

if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')


    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')

    ur.log_out()
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
