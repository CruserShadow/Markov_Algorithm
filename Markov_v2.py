import json
import re

with open("Rules.json", "r") as file:
    rules = [json.load(file)]

for key, item in rules[0].items():
    print(f"{key} -> {item}")
print()

word = input("Word -> ")
print(f"> {word} <")

#  переменные для цикла
end = False

for loops in range(150):

    for check, change in rules[0].items():

        if check in word:
            if "." in change:
                change = change.replace(".", "")
                word = re.sub(check, change, word, 1)
                end = True
                print(word)
                break

            word = re.sub(check, change, word, 1)
            print(word)
            break

    if end:
        break