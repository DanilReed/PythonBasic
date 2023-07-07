# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

one = 1
two = 2
nine = 9
ten = 10
one_hundred = 100
thousand = 1000
x1 = 0
x2 = 0
x3 = 0
wrong = "Не входит в диапазон"


while True:

    number = int(input("Введите число от 1 до 999>"))

    if one <= number <= nine:
        result = number ** two

    elif ten <= number < one_hundred:
        x1 = number % 10
        x2 = number // 10
        result = x1 * x2

    elif one_hundred <= number < thousand:
        x1 = number % 10
        x2 = number % 100 // 10
        x3 = number // 100
        number = str(x1) + str(x2) + str(x3)
        result = number

    else:
        result = wrong

    print(result)
    break
