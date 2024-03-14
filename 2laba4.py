import random
right = 0
false = 0
while false < 3:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    rez = n1 + n2
    otvet = input(f"{n1} + {n2} = ")
    if otvet.isdigit() and int(otvet) == rez:
        print("Правильно!")
        right += 1
    else:
        print("Ответ неверный")
        false += 1
print(f"Игра окончена. Правильных ответов: {right}")
