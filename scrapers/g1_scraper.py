import requests
from bs4 import BeautifulSoup

def scrape_g1():
    url = "https://g1.globo.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = []

            for item in soup.find_all('a', class_='feed-post-link'):
                titulo = item.text.strip() if item.text else "Sem título"
                link = item.get('href')
                if link:
                    noticias.append({'titulo': titulo, 'link': link})
            return noticias
        else:
            print(f"Erro ao acessar o G1: {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro no scraper do G1: {e}")
        return []