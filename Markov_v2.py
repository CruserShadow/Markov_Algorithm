import json
import re

with open("Rules.json", "r") as file:
    raw_rules = json.load(file).get("rules")

letters = []
for atr in raw_rules:
    letters.append([atr.get(x) for x in atr])

rule = dict(letters)

for key, item in rule.items():
    print(f"{key} -> {item}")


word = input("Word -> ")
print(f"> {word} <")


#  переменные для цикла
end = False

for loops in range(150):

    for check, change in rule.items():
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
