'''
This code downloads dog breeds descriptions from https://wamiz.pl/pies/rasy.
'''
import requests
from bs4 import BeautifulSoup

def get_breeds_urls(url: str, class_name:str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        elements = soup.find_all('a', class_=class_name) 
        hrefs = [element['href'] for element in elements if 'href' in element.attrs]
        
        return hrefs
    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania strony: {e}")
        return []

def get_breed_description(url: str, tag_name = 'p', class_name = 'clamp-wrapper tw-break-words tw-my-3') -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        elements = soup.find_all('div', class_=class_name)
        texts = [element.find(tag_name).get_text(separator='\n') for element in elements if element.find(tag_name)]
        text = ' '.join(texts)
        text = text.replace(u'\xa0', u' ')
        text = text.replace(u'\n', u' ')
        return text

    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania strony: {e}")
        return 'error'

if __name__ == "__main__":

    url = 'https://wamiz.pl/pies/rasy'
    relative_links = get_breeds_urls(url, 'listView-item-title--homepageBreed')

    full_links = []
    breed_names = []
    for link in relative_links:
        full_link = 'https://wamiz.pl' + link
        full_links.append(full_link)
        breed_name = full_link.rstrip('/').split('/')[-1]
        breed_names.append(breed_name)
    links_to_save = '\n'.join(full_links)
    breed_names_to_save = '\n'.join(breed_names)
    with open('../dog_breeds_links.txt', 'w') as f:
        f.write(links_to_save)

    with open('dog_breeds.txt', 'w') as f:
        f.write(breed_names_to_save)

    breed_descriptions = []
    for link in full_links:
        description = get_breed_description(link)
        print(description)
        breed_descriptions.append(description)
    descriptions_to_save = '\n'.join(breed_descriptions)
    with open('../dog_breeds_descriptions.txt', 'w') as f:
        f.write(descriptions_to_save)
