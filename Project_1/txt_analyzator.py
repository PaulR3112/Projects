"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Ryzner
email: pavel.ryzner@gmail.com
discord: Pavel.R

"""
import string

TEXTS = [

"""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",

""" At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",

"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""

]

#zadať vstupné údaje
username = input("username: ")
password = input("password: ")

# slovník uživatelia a ich hesla účtov
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

# kontroluje, či uživatel je v slovníku. Vstup == heslo
if username in users and users[username] == password:
    print("-"*40)
    print("Welcome to the app", username,)
    print("We have 3 texts to be analyzed")
    print("-"*40)
else:
    print("Unregistered user, terminating the program..")
    exit() # ukončí sa program


# definovanie možnosti pre výber z listu "TEXTS" iba digit.
while True:
    options = input("Enter a number btw. 1 and 3 to select: ")
    if options.isdigit() and int(options) in [1,2,3]:
        options = int(options)
        break
    else:
        print("Did you choose a number out of range, or did you use text")
        exit() # ukončí sa program
        
# kompletný výpis
selected_text = TEXTS[options - 1]

# odstránenie interpunkcie
interpunct = str.maketrans('', '', string.punctuation)
clean_text = selected_text.translate(interpunct)

# čistý text
words = clean_text.split()
word_count = len(words)

titlecase = sum(1 for word in words if word.istitle())
uppercase = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase = sum(1 for word in words if word.islower())
numeric =  [word for word in words if word.isdigit()]
numeric_count = len(numeric)
numbers = sum(int(num) for num in numeric)

print("-"*40)

#print(selected_text) # nie je potrebné vypisovať celý text !!!
print(f" There are {word_count} words in selected text.")
print(f" There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"There sum all the numbers {numbers}")

print("-"*40)

# tabulka
print("LEN|  OCCURENCES  |NR.")
print("-" * 40)

word_lenghts = [len(word) for word in words]
length_count = {}
for length in word_lenghts:
    if length in length_count:
        length_count[length] +=1
    else:
        length_count[length] =1

for length in sorted(length_count):
    count = length_count[length]
    print(f"{length :>3}|{'*' * count:<15}|{count}")













