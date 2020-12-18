import json

with open("Rules", "r") as file:
    rules = json.load(file)

list_of_checkwords = list(rules.keys())  # проверяемые
list_of_changewords = list(rules.values())  # заменяемые
kolvo_pravil = len(list_of_checkwords)

# ввод
word = input("Слово -> ")

for i in range(0, kolvo_pravil):
    print(f"{list_of_checkwords[i]} -> {list_of_changewords[i]}")
print()

print(f"> {word} <")

#  переменные для цикла while
i = 0
loops = 0
end = False

while i < len(list_of_changewords):
    restart = False

    for q in range(0, len(word)):  # q - номер символа в строке

        if word[q:q + len(list_of_checkwords[i])] == list_of_checkwords[i]:  # проверка подстроки на соответсвие правилу

            if "." in list_of_changewords[i]:   # проверка на наличие точки в правиле
                list_of_changewords[i] = list_of_changewords[i].replace(".", "", 1)
                end = True

            word = word[:q] + list_of_changewords[i] + word[q + len(list_of_checkwords[i]):]  # замена подстроки
            #  word = word.replace(list_of_checkwords[i], list_of_changewords[i],1)

            restart = True
            loops += 1
            i = 0
            print(word)
            break

    if end:
        break

    if loops == 100:
        print(f"Rule has infinite cycle {list_of_checkwords[i]} -> {list_of_changewords[i]} / completed {loops} times")
        del list_of_changewords[i]
        del list_of_checkwords[i]
        loops = 0
        break

    if i < kolvo_pravil and restart is False:
        i += 1
