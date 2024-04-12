best_score = 0
total_friends = 0

while True:
    score = int(input("Введите результат игрока (или -1 для завершения): "))

    if score == -1:
        break

    if score > best_score:
        best_score = score
    total_friends += 1

print("Лучший результат игры в боулинг:", best_score)
print("Общее количество друзей в боулинге:", total_friends)