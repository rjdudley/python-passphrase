import random
import csv

def roll():
    one = random.randint(1,6)
    two = random.randint(1,6)
    three = random.randint(1,6)
    four = random.randint(1,6)
    five = random.randint(1,6)

    return f"{one}{two}{three}{four}{five}"

def word():

    key = roll()
    with open('wordlist.csv', mode='r') as infile:
        reader = csv.reader(infile)
        wordlist = {rows[0]:rows[1] for rows in reader}

    return wordlist[key]

def suffix():
    one = random.randint(1,6)
    two = random.randint(1,6)

    return f"{one}{two}"