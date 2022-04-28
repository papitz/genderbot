import csv
import string

dictonary = {}
with open("words.csv") as wordlist:
    csv_reader = csv.reader(wordlist, delimiter=",")
    for row in csv_reader:
        if len(row) <= 1:
            # skip words without translation
            continue
        else:
            dictonary.update({row[0].casefold(): row[1].split(";")})

print(dictonary)

with open("grundlagen.tex") as input:
    lines = input.readlines()
    line_number = 0
    for line in lines:
        line_number += 1
        line_without_punctuation = line.translate(
            str.maketrans("", "", string.punctuation)
        )
        words = line_without_punctuation.split()
        for word in words:
            if word.casefold() in dictonary:
                print(
                    f"{word} in Zeile {line_number} ist nicht gegendert. Alternativen: {dictonary[word.casefold()]}"
                )
