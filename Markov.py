import json
import re

with open("Rules.json", "r") as file:
    rules = [x for x in json.load(file).items()]

count = len(rules)
check = [i[0] for i in rules]
change = [i[1] for i in rules]

for i in range(0, count):
    print(f"{check[i]} -> {change[i]}")
print()

word = input("Word -> ")
print(f"> {word} <")

#  переменные для цикла while
i = 0
loops = 0

while i < count:
    restart = False

    if check[i] in word:

        if "." in change[i]:
            change[i] = change[i].replace(".", "")
            word = re.sub(check[i], change[i], word, 1)
            print(word)
            break

        word = re.sub(check[i], change[i], word, 1)
        restart = True
        loops += 1
        print(word)

    if loops == 100:
        print(f"Rule has infinite cycle {check[i]} -> {change[i]} | completed {loops} times")
        break

    if restart is True:
        i = 0
    elif restart is False:
        i += 1
