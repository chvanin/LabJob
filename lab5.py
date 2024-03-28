# Объявляем переменные и присваиваем им значения
# a будет равно 9
a = 9

# b будет равно 15.4
b = 15.4

# c будет равно "abcdefg"
c = "abcdefg"

# d будет равен списку [1, 2, 3, 4, 5, 6]
d = [1, 2, 3, 4, 5, 6]

# e будет равен кортежу (1, 2, 3, 4, 5, 6)
e = (1, 2, 3, 4, 5, 6)

# f будет равен строке "123456"
f = str(d)

# g будет равен строке "12345"
g = "12345"

# h будет равен целому числу 12345
h = int(g)

# j будет равен списку символов "abcdefg"
j = list(c)

# Определяем функцию summ, которая принимает два аргумента a и b и возвращает сумму этих аргументов
def summ(a, b):
    # Выводим сумму a и b
    print(a + b)

# Вызываем функцию summ с аргументами 10 и 14
summ(10, 14)

# Переменная a инициализируется значением 0
a = 0

# Используем цикл for для увеличения a на 1 пять раз
for i in range(5):
    # Увеличиваем a на 1
    a += 1
    # Выводим значение a
    print(a)

# Снова инициализируем переменную a значением 0
a = 0

# Используем цикл while для увеличения a на 1 до тех пор, пока a меньше 5
while a < 5:
    # Увеличиваем a на 1
    a += 1
    # Выводим значение a
    print(a)

# Инициализируем переменные a, b и c значениями 1, 2 и 154 соответственно
a = 1
b = 2
c = 154

# Проверяем условия и выводим соответствующее сообщение
if a > 2:
    print("a > 2")
elif b > 3:
    print("b > 3")
else:
    print("c > a and b")

# Запрашиваем у пользователя ввод числа смурфиков
smurfs = input("Введите число смурфиков: ")

# Проверяем введенное число и выводим соответствующее сообщение
if 0 < smurfs <= 10:
    print("В деревне побывал Гаргамель")
elif 11 < smurfs < 20:
    print("Смурфики в путешествии")
elif 21 < smurfs < 50:
    print("Деревня процветает")
elif 51 < smurfs < 100:
    print("В деревне праздник, все в сборе")
else:
    print("В деревне кипит жизнь")

# Попытка разделить число a на число b и вывод сообщения об ошибке в случае возникновения ошибки деления на ноль
try:
    a = 1
    b = 0
    c = a / b
except:
    print("error")
