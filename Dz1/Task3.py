# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.



a = int(input("Введите сторонy треугольника a >"))
b = int(input("Введите сторонy треугольника b >"))
c = int(input("Введите сторонy треугольника c >"))

if a + b> c and c + a > b and b + c > a:
    if a == b == c:
        print("Такой треугольник равносторонний")
    elif a == b or a == c or c == b:
        print("Такой треугольник равнобедреный")
    elif a != b != c:
        print("Такой треугольник разносторонний")
else:
    print("Такого треугольника несуществует")

