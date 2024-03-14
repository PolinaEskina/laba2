N = int(input("Введите кол-во слов: "))
s = ""
for i in range(N):
    slovo = input("Введите слово: ")
    if i == 0:
        s += slovo
    else:
        s += (" " + slovo)
print(s)
