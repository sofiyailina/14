'''В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
Для найденного значения x вычислите частное от деления значения арифметического выражения на 14 и укажите его в ответе в десятичной системе счисления.
Основание системы счисления в ответе указывать не нужно.'''

digits = '0123456789ABCDE'
for x in digits:
        n1 = int(f"123{x}5")
        n2 = int(f"1{x}233")
        if (n1 + n2) % 14 == 0:
            print(n1 ,n2)
            break