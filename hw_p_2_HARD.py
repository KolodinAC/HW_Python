# Задача №2_HARD Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.

def is_int(string):   # создал функцию проверки является ли число int
    try:
        int(string)
        return True
    except:
        return False

number = input('Введите желаемое целое или разделенное точкой вещественное число: ')

try:
    if is_int(number) == True:
        sum = 0
        number = abs(int(number))    # избавился от минуса
        while (number != 0):
            sum = sum + int(number) % 10
            number = int(number) // 10
        print("Сумма цифр вашего числа равна: ", sum)
    else:
        number = number.replace('-', '')  # избавился от минуса
        x = number.split('.')
        a = int(x[0])
        b = int(x[1])
        sum2 = 0
        while a != 0:
            sum2 = sum2 + a % 10
            a = a // 10
        while b != 0:
            sum2 = sum2 + b % 10
            b = b // 10
        print("Сумма цифр вашего числа равна: ", sum2)
except:
    print('Вы ввели некорректные данные!')

