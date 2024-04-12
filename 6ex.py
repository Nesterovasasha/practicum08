N = int(input("Введите натуральное число N: "))

for i in range(1, N+1):
    spaces = " " * (N - i)
    stars = "*" * i
    print(spaces + stars)