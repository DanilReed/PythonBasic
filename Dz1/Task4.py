# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.def prime_num(number):
#

def prime_num(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range (3, int((num** 0.5)) +1, 2):
        if num % i == 0:
            return False
    return True

number = int(input("Введите число>"))

if number < 0 or number > 100000:
    print ("Недопустимое число")
else:
    print(f"{prime_num(number)}")