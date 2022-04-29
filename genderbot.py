import csv
import string
import sys
from termcolor import colored

dictonary = {}
with open("words.csv") as wordlist:
    csv_reader = csv.reader(wordlist, delimiter=",")
    for row in csv_reader:
        if len(row) <= 1:
            # skip words without translation
            continue
        else:
            dictonary.update({row[0].casefold(): row[1].split(";")})

input_files = sys.argv[1:]

for file in input_files:
    print(colored(f"\nReading from file {file}\n", "green"))
    with open(file) as input_file:
        lines = input_file.readlines()
        line_number = 0
        with open("gendered_" + file, "w") as output:
            for line in lines:
                line_number += 1
                line_without_punctuation = line.translate(
                    str.maketrans("", "", string.punctuation)
                )
                words = line_without_punctuation.split()
                for word in words:
                    if word.casefold() in dictonary:
                        alternatives = dictonary[word.casefold()]
                        print(
                            f"{word} in Zeile {line_number} ist nicht gegendert. Alternativen:"
                        )
                        alt_count = 0
                        for alternative in alternatives:
                            print(f"{alt_count}. {alternative}")
                            alt_count += 1
                        user_input = input("Korrigieren? (n/<number of correction>)> ")
                        if user_input == "n":
                            continue
                        elif user_input.isdecimal():
                            if int(user_input) < len(alternatives):
                                line = line.replace(word, alternatives[int(user_input)])
                        else:
                            print(
                                colored(
                                    f"Input {user_input} kann nicht verarbeitet werden",
                                    "red",
                                )
                            )

                output.write(line)
