"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Pavel Ryzner
email: pavel.ryzner@gmail.com
discord: Pavel.R

"""

import random

# Pozdrav
print("Hi there!")
print("-" * 47)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print("-" * 47)

# Funkcia vyvtorenie náhodneho 4-ciferneho cisla
def vytvor_tajne_cislo():
    cislice = list(range(10))
    random.shuffle(cislice)
    while cislice[0] == 0:
        random.shuffle(cislice)
    tajne_cislo = cislice[:4]
    tajne_cislo_str = ''
    for cislica in tajne_cislo:
        tajne_cislo_str += str(cislica)
    return tajne_cislo_str

# Kontrola spravnosti vstupu 
def skontroluj_vstup(vstup):
    if len(vstup) != 4:
        print("The input must have exactly 4 digits.")
        return False
    if not vstup.isdigit():
        print("Input must contain digits only.")
        return False
    if vstup[0] == '0':
        print("The number must not start with zero.")
        return False
    if len(set(vstup)) != 4:
        print("Digits must be unique.")
        return False
    return True

# Vyhodnotenie tipu
def vyhodnot_tip(tajne_cislo, tip):
    bulls = 0
    cows = 0
    for i in range(len(tajne_cislo)):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

def hodnotenie_pokusov(pokusy):
    if pokusy <= 4:
        return "amazing"
    elif pokusy <= 7:
        return "average"
    else:
        return "not so good"

# Hlavný kód
tajne_cislo = vytvor_tajne_cislo()
pokusy = 0

while True:
    print("Enter a number:")
    print("-" * 47)
    tip = input(">>> ")
    if not skontroluj_vstup(tip):
        continue
    
    pokusy += 1
    bulls, cows = vyhodnot_tip(tajne_cislo, tip)
    
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {pokusy} guesses!")
        print("-" * 47)
        print(f"That's {hodnotenie_pokusov(pokusy)}")
        print("-" * 47)
        break
    else:
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print("-" * 47)