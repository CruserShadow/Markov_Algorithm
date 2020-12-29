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


#  переменные для цикла
end = False

for loops in range(100):

    for i in range(count):

        if check[i] in word:
            if "." in change[i]:
                change[i] = change[i].replace(".", "")
                word = re.sub(check[i], change[i], word, 1)
                end = True
                print(word)
                break

            word = re.sub(check[i], change[i], word, 1)
            print(word)
            break

    if end:
        break


