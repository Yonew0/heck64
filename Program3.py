import time
from sys import argv

comps_list = ["desktop-ancholav", "zmeuka-pc", "sovin-sovin-u4ilk228_Pc"]

def start():
	print("""
		Program3, IAVN-UEBUNTU
		Введите имя ПК в аргументах программы.
		Аргумент -P - режим разработчика.""")

def vzlom(arg: str):
	print("Получение дополнительной информации сети...")
	time.sleep(2)
	if arg.lower() in comps_list:
		for i in range(101):
			print(f"\nИмпорт данный с ПК {arg}, {i}%")
			print(f"Оставшееся время: {100 - i} секунд")
			time.sleep(1)
		print("Успех!")
		input()
	elif arg.lower() == '-p':
		programer_input = input("Введите имя ПК к которому хотите подключится: ")
		for i in range(101):
			print(f"\nИмпорт данный с ПК {programer_input}, {i}%")
			print(f"Оставшееся время: {100 - i} секунд")
			time.sleep(1)
		print("Успех!")
		input()
	else:
		print(f"Невозможно подключится к этому ПК. Возможно, вы имели в виду \n{comps_list}?")
		input()

start()

try:
	vzlom(argv[1])
except IndexError:
	print("В аргументах ничего нет.")
	input()