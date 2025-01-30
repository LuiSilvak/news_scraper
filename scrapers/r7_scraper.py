import requests
from bs4 import BeautifulSoup

def scrape_r7():
    url = "https://noticias.r7.com/"
    try:    
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = []

            # Depuração: Verificar elementos encontrados
            elementos = soup.find_all('div', class_='layout-container')
            print(f"Elementos encontrados na CNN: {len(elementos)}")

            for item in elementos:
                titulo = item.text.strip() if item.text else "Sem título"
                link = item.get('href')
                if link:
                    if not link.starswith("http"):
                        link = f"https://noticias.r7.com/{link}"
                    noticias.append({'titulo': titulo, 'link': link})
                else:
                    print("Elemento encontrado sem 'href'")
            return noticias
        else:
            print(f"Erro ao acessar o R7 {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro no scraper do R7: {e}")
        return []