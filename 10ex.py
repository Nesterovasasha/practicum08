def perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

N = int(input("Введите число N: "))

print("Совершенные числа до", N, "включительно:")
for i in range(2, N+1):
    if perfect_number(i):
        print(i)