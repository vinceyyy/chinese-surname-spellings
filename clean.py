from os import write


surnames = []
with open("surname.txt") as f:
    for line in f:
        l = line.strip().split("\t")
        surnames += l[1:]

with open("surnames.txt", "a") as f:
    for surname in surnames:
        f.write(
            surname + "\n",
        )
