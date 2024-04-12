def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_up_to_n(N):
    prime_list = []
    for i in range(2, N + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

N = int(input("Введите число N: "))
prime_list = prime_numbers_up_to_n(N)
print("Простые числа до", N, ":", prime_list)