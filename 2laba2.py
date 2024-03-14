s = ""
slovo = ""
while slovo != "stop":
    slovo = input("Введите слово: ")
    if s == "":
        s += slovo
    else:
        s += (" " + slovo)
print(s[:-4])