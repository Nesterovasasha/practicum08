total_income = 0
count = 0

while True:
    income = input("Введите месячный доход жителя (для завершения введите '0'): ")

    if income == '0':
        break

    total_income += float(income)
    count += 1

if count == 0:
    print("Нет данных для расчета среднего дохода.")
else:
    average_income = total_income / count
    print("Средний доход жителей города: ", average_income)