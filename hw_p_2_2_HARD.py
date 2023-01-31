# Задача №2_HARD Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.

def is_int(string):
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
        sum2 = 0
        res = 0
        i = len(number) - 2
        number = float(number)
        while i !=0:
            number = number * 10
            i -= 1
        res = round(number, 1)
        res = abs(res)
        while (res != 0):
            sum2 = sum2 + int(res) % 10
            res = int(res) // 10
        print("Сумма цифр вашего числа равна: ", sum2)
except:
    print('Вы ввели некорректные данные!')

