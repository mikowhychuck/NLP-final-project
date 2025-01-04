import requests
from bs4 import BeautifulSoup
def get_labrador_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Słownik na wyciągnięte informacje
    labrador_info = []

    # Wyciąganie "Rys historyczny"
    historical_section = soup.find("h2", id="Rys_historyczny")
    if historical_section:
        historical_text = historical_section.find_next("p").text.strip()
        labrador_info.append(historical_text)

    # Wyciąganie "Wygląd"
    appearance_section = soup.find("h2", id="Wygląd")
    if appearance_section:
        appearance_text = appearance_section.find_next("ul").text.strip()
        labrador_info.append(appearance_text)

    # Wyciąganie "Zachowanie i charakter"
    behavior_section = soup.find("h2", id="Zachowanie_i_charakter")
    if behavior_section:
        behavior_text = behavior_section.find_next("p").text.strip()
        labrador_info.append(behavior_text)

    # Wyciąganie "Zdrowie i pielęgnacja"
    health_section = soup.find("h2", id="Zdrowie_i_pielęgnacja")
    if health_section:
        health_text = health_section.find_next("p").text.strip()
        labrador_info.append(health_text)

    # Wyciąganie "Użytkowość"
    usability_section = soup.find("h2", id="Użytkowość")
    if usability_section:
        usability_text = usability_section.find_next("p").text.strip()
        labrador_info.append(usability_text)

    return labrador_info
# URL strony z Wikipedii
for piesek in [
    "Labrador_retriever",
    "Yorkshire_terrier",
    "Owczarek_niemiecki",
    "Beagle",
    "Golden_retriever",
    "Buldog_francuski",
    "Mops_(rasa_psa)",
    "Cocker_spaniel_angielski",
    "Shih_tzu",
    "Border_collie",
    "Maltańczyk",
    "Rottweiler",
    "Doberman",
    "Akita_inu",
    "Husky_syberyjski",
    "Chihuahua_(rasa_psa)"
]:
    pies= piesek
    URL = f"https://pl.wikipedia.org/wiki/{pies}"
    # Wywołanie funkcji
    labrador_data = get_labrador_info(URL)

    file = open(f"dog_descriptions.txt", "a", encoding="utf-8")
    file.write(f"{labrador_data}\n")
    # # Wyświetlanie wyników
    # for content in labrador_data:
    #     file.write(f"{content}")

