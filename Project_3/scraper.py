"""¨
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Pavel Ryzner 
email: pavel.ryzner@gmail.com
discord: Paul33 paul335110

"""

import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import html
import os

def validate_arguments():
    """Overenie správnosti argumentov."""
    if len(sys.argv) != 3:
        print("Použitie: python scraper.py <URL> <output_file.csv>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    if not url.startswith("https://www.volby.cz/"):
        print("Chyba: Zadajte platnú URL adresu zo stránky volby.cz.")
        sys.exit(1)
    
    if not output_file.endswith(".csv"):
        print("Chyba: Výstupný súbor musí mať príponu .csv.")
        sys.exit(1)

    # Nastavenie uložiska
    output_path = os.path.join("C:\\Users\\Home\\Downloads", output_file)
    return url, output_path

def download_data(url):
    """Stiahnutie HTML obsahu zo stránky."""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Chyba: stránku sa nepodarilo načítať (status {response.status_code}).")
        sys.exit(1)

    response.encoding = response.apparent_encoding
    return response.text

def parse_main_page(html):
    """Extrahuje odkazy stránky obcí v detaile."""
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')
    links = []

    base_url = "https://www.volby.cz/pls/ps2017nss/"

    for row in rows[2:]:
        cells = row.find_all('td')
        if len(cells) > 0:
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link_element = cells[0].find('a')
            if link_element is not None:
                relative_link = link_element['href']
                full_link = base_url + relative_link
                links.append((code, name, full_link))
            else:
                print(f"Upozornenie: Obec {name} (kód: {code}) nemá odkaz na detail stránky.")

    return links

def safe_extract(soup, headers):
    """Extrahuje text na základe atribútu "headers"."""
    element = soup.find('td', headers=headers)
    return element.text.strip() if element else "N/A"

def parse_obec_page(html_content):
    """Extrahuje údaje o konkrétnej obci."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Získanie údajov o voličoch a jeho hlasoch
    registered = safe_extract(soup, "sa2")
    envelopes = safe_extract(soup, "sa3")
    valid = safe_extract(soup, "sa6")

    # Hlasy - jednotlivé strany
    parties = [html.unescape(header.text.strip()) for header in soup.find_all('td', headers="t1sa1 t1sb2")]
    votes = [cell.text.strip() for cell in soup.find_all('td', headers="t1sa2 t1sb3")]

    return registered, envelopes, valid, parties, votes

def save_to_csv(data, output_file, parties):
    """Uloží extrahovaný súbor do .csv."""
    if not data:
        print("Chyba: Žiadne údaje neboli extrahované.")
        sys.exit(1)

    # Hlavička CSV súboru
    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + parties

    df = pd.DataFrame(data, columns=header)
    df.to_csv(output_file, index=False, encoding='utf-8-sig', sep=';')
    print(f"Výsledky boli uložené do súboru: {output_file}")

if __name__ == "__main__":
    url, output_file = validate_arguments()
    main_page_html = download_data(url)
    links = parse_main_page(main_page_html)
    all_data = []
    all_parties = []

    for code, name, link in links:
        print(f"Spracovávam obec: {name} (kód: {code})")
        obec_html = download_data(link)
        registered, envelopes, valid, parties, votes = parse_obec_page(obec_html)

        if not all_parties:
            all_parties = parties

        all_data.append([code, name, registered, envelopes, valid] + votes)

    save_to_csv(all_data, output_file, all_parties)