import time


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if User(nickname, hash(password), 0) in self.users:
            if hash(password) == self.users[self.users.index(User(nickname, hash(password), 0))].password:
                self.current_user = self.users[self.users.index(User(nickname, hash(password), 0))]
            else:
                print('Пароль введен неверно')
        else:
            print('Имя пользователя введено неверно')

    def register(self, nickname, password, age):
        if User(nickname, hash(password), age) in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, hash(password), age))
            self.current_user = User(nickname, hash(password), age)

    def log_out(self):
        print(f'Выход выполнен успешно, досвидания {self.current_user}')
        self.current_user = None

    def add(self, *args):
        for i in range(len(args)):
            if args[i] in self.videos:
                pass
            else:
                self.videos.append(args[i])

    def get_videos(self, word):
        title_list = []
        for i in self.videos:
            if word in i:
                title_list.append(i.title)
        return title_list

    def watch_video(self, title):
        if Video(title) in self.videos:
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                if self.current_user.age < 18 and self.videos[self.videos.index(Video(title))].adult_mode == True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(1, self.videos[self.videos.index(Video(title))].duration + 1):
                        self.videos[self.videos.index(Video(title))].time_now = i
                        time.sleep(1)
                        print(self.videos[self.videos.index(Video(title))].time_now)
                    self.videos[self.videos.index(Video(title))].time_now = 0
                    print('Конец видео')


class Video:
    def __init__(self, title, duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item.lower() in self.title.lower()


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname


#
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

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
