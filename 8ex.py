digits = [str(i) for i in range(1, 10)]

for i in range(1, 10):
    num_str = ''.join(digits[:i])
    result = int(num_str) * 8 + i
    print(f"{num_str} * 8 + {i} = {result}")

print()

for i in range(1, 10):
    num_str = ''.join(digits[:i])
    result = int(num_str) * 9 + i + 1
    print(f"{num_str} * 9 + {i + 1} = {result}")

print()

for i in range(1, 10):
    num_str = '1' * i
    if i == 1:
        result = int(num_str)
    else:
        result = int(num_str) * int(num_str)
    print(f"{num_str} * {num_str} = {result}")