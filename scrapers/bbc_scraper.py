import requests
from bs4 import BeautifulSoup

def scrape_bbc():
    url = "https://www.bbc.com/portuguese"
    try:    
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = []

            # Depuração: Verificar elementos encontrados
            elementos = soup.find_all('a', class_='bbc-1i4ie53 e1d658bg0')
            print(f"Elementos encontrados na CNN: {len(elementos)}")

            for item in elementos:
                titulo = item.text.strip() if item.text else "Sem título"
                link = item.get('href')
                if link:
                    if not link.startswith("http"):
                        link = f"https://www.bbc.com/portuguese{link}"
                    noticias.append({'titulo': titulo, 'link': link})
                else:
                    print("Elemento encontrado sem 'href'")

            return noticias
        
        else:
            print(f"Erro ao acessar a BBC: {response.status_code}")
            return []
        
    except Exception as e:
        print(f"Erro no scraper da BBC: {e}")
        return []