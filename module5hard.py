
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
	def __init__(self, users, videos, current_user):
		self.users = users
		self.videos = videos
		self.current_user = current_user

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
	for video in videos:
		if video.title == title:
			self.videos.append(video_object)
def get_videos(self, title):
	videos_list = [video['name'] for video in self.videos if title in video['name']]
	return videos_list

def watch_video(self, title):
	for video in videos:
		if video.title != title:
			break