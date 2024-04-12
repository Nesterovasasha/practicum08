N = int(input("Введите число N: "))
perfect_numbers = 0

for num in range(2, N + 1):
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i

    if divisors_sum == num:
        perfect_numbers += 1

print("Количество совершенных чисел в интервале от 2 до", N, ":", perfect_numbers)