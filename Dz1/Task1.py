# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

julian_calendar = 1582
test_julian = 4
Gregorian_test_one = 400
Gregorian_test_two = 100


year = int(input('Введите год>'))

if year < julian_calendar:
   if not year % test_julian:
       print("Високосный год")
   else:
       print("Не Високосный год")
elif year % Gregorian_test_two and not year % test_julian or year % Gregorian_test_one == 0:
    print("Високосный год")
else:
    print("Не Високосный год")

