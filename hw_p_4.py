# Задача №8 Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


try:
    n = int(input('Введите длину шоколадки: '))
    m = int(input('Введите ширину шоколадки: '))
    k = int(input('Введите желаемое количество долек: '))

    if n > 0 and m > 0 and k > 0:
        if k < m * n and (k % m == 0 or k % n == 0):
            print('Вы сможете отломить столько долек')
        else:
            print('У вас не получится отломить столько долек одним куском')
    else:
        print('Введите корректное число долек!')
except:
    print('Вы ввели некорректные данные!')