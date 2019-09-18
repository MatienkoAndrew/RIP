# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

# def timer():
# 	import time
#
# 	def wrapper(*args, **kwargs):
# 		t = time.clock()
# 		res = func(*args, **kwargs)
# 		print(func.__name__, time.clock() - t)
# 		return res
# 	return wrapper

# Декоратор, вычисляющий время выполнения функции

def timer(func):
	import time

	def wrapper(*args, **kwargs):
		t = time.time()
		res = func(*args, **kwargs)
		print("Function " + str(func.__name__) + " : " + str(time.time() - t) + "(sec)")
	return wrapper
