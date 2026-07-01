import requests

from programs import get_list

code = input("Напишите код программы: ")
quote = int(input("Напишитие номер вашей квоты:\n1 (Бюджетная основа)\n2 (Контракт)\n3 (Особое право)\n4 (Отдельная квота)\n5 (Целевой приём)\n"))

print(get_list(quote, code))