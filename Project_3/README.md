
## **Popis projektu**

Tento projekt automatizuje sťahovanie a spracovanie údajov zo stránky **volby.cz**, pričom:

1. Sťahuje údaje o volebných výsledkoch do Poslaneckej snemovne z roku 2017 v Českej republike.
2. Tieto údaje ukladá do súboru `.csv`.

## **Inštalácia knižníc**

Pred použitím skriptu je potrebné nainštalovať knižnice uvedené v súbore `requirements.txt`.

### **Kroky:**

1. **Vytvorenie virtuálneho prostredia (Windows)**

   python -m venv Projekt  # Projekt je moje uložisko
   Projekt\Scripts\activate.bat  # Upozornenie: pre Windows použite .bat

2. **Innštalácia knižníc zo súboru `requirements.txt`**
   
   pip install -r requirements.txt
   pip freeze > requirements.txt
   pip install requests beautifulsoup4 pandas

### **Formát príkazu pre spustenie:**

python scraper.py <URL> <výstupný_súbor.csv>

### **Argumenty:**

1. `<URL>` – "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101"
2. `<výstupný_súbor.csv>` – vysledky_budejovice.csv


### **Spustenie programu:**

python scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101" vysledky_budejovice.csv


## **Ako stiahnuť `.csv` súbor**

Po úspešnom spustení skriptu:

1. **Výstupný súbor**:
   - Výsledky sa uložia do súboru `.csv` so zadaným názvom (napr. `vysledky_budejovice.csv`).
2. **Prístup k súboru**:
   - Súbor sa nachádza v rovnakom adresári, ako bol spustený skript.
3. **Otváranie `.csv` súboru**:
   - Môžeš ho otvoriť v Exceli
