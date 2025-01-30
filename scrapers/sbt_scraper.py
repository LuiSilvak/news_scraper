import requests
from bs4 import BeautifulSoup

def scrape_sbt():
    url = "https://sbtnews.sbt.com.br/noticias"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = []

            # Depuração: Verificar elementos encontrados
            elementos = soup.find_all('a', class_='headline-link')
            print(f"Elementos encontrados na CNN: {len(elementos)}")

            for item in elementos:
                titulo = item.text.strip() if item.text else "Sem título"
                link = item.get('href')
                if link:
                    if not link.startswith("http"):
                        link = f"https://sbtnews.sbt.com.br/noticias{link}"
                    noticias.append({'titulo': titulo, 'link': link})
                else:
                    print("Elemento encontrado sem 'href'")
            return noticias
        else:
            print(f"Erro ao acessar o SBT News: {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro no scraper do SBT News: {e}")
        return []