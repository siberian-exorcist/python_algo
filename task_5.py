"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

print('Введите диапазон букв\n')
a = str(input('Введите первую букву = ')).lower()
b = str(input('Введите вторую букву = ')).lower()
print(f'Позиция первой буквы в алфавите = {ord(a)-96}')
print(f'Позиция второй буквы в алфавите = {ord(b)-96}')
print(f'Количество букв между {a} и {b}  = {ord(a) - ord(b) - 1 if a > b  else ord(b) - ord(a) - 1 if a < b else "0"}')

