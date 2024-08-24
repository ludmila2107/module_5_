import time


class User:
	def __init__(self, nickname, password, age):
		self.nickname = nickname
		self.password = hash(password)
		self.age = age


class Video:
	def __init__(self, title, duration, time_now=0, adult_mode=False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = adult_mode


class UrTube:
	def __init__(self):
		self.users = []
		self.videos = []
		self.current_user = None

	def log_in(self, nickname, password):
		for user in self.users:
			if user.nickname == nickname:
				if user.password == hash(password):
					self.current_user = user
				else:
					print('Неверный пароль')
			else:
				print('Пользователь с таким ником не найден')

	def register(self, nickname, password, age):
		for user in self.users:
			if user.nickname == nickname:
				print(f"Пользователь {nickname} уже существует")
				return

		user = User(nickname, password, age)
		self.users.append(user)
		self.current_user = user

	def log_out(self):
		self.current_user = None
		print('Cброс текущего пользователя')

	def add(self, *video_object):
		for video in video_object:
			if video not in self.videos:
				self.videos.append(video)

			else:
				print('Такой фильм уже есть')

	def get_videos(self, title):
		title = title.lower()
		video_list = []

		for video in self.videos:
			if title in video.title.lower():
				video_list.append(video.title)
		return video_list

	def watch_video(self, title):
		count = 0
		if self.current_user == None:
			print('Войдите в аккаунт, чтобы смотреть видео')
			return
		for video in self.videos:
			if video.title == title:
				if (video.adult_mode == True and self.current_user.age >= 18) or (video.adult_mode == False):
					print('можно смотреть')
					while video.duration > count:
						time.sleep(1)
						count += 1
						print(count)

					else:
						print('Конец видео')
						count = 0
				else:
					print('Вам нет 18 лет, пожалуйста покиньте страницу')




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
