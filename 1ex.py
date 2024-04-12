best_score = 0

while True:
    score = int(input("Введите результат игрока (или -1 для завершения): "))

    if score == -1:
        break

    if score > best_score:
        best_score = score

print("Лучший результат игры в боулинг:", best_score)