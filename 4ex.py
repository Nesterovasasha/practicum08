X = int(input("Введите целое число X: "))
total_sum = 0

for i in range(1, X+1):
    total_sum += i
    print("Сумма первых", i, "натуральных чисел равна", total_sum)