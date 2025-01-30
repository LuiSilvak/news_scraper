import requests
from bs4 import BeautifulSoup

def scrape_cnn():
    url = "https://www.cnnbrasil.com.br/politica/"
    try:    
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = []

            # Depuração: Verificar elementos encontrados
            elementos = soup.find_all('a', class_='home__list__tag')
            print(f"Elementos encontrados na CNN: {len(elementos)}")

            for item in elementos:
                titulo = item.text.strip() if item.text else "Sem título"
                link = item.get('href')
                if link:
                    if not link.startswith('http'):
                        link = f"https://www.cnnbrasil.com.br/politica/{link}"
                    noticias.append({'titulo': titulo, 'link': link})
                else:
                    print("Elemento encontrado sem 'href'")
                    
            return noticias
        
        else:
            print(f"Erro ao acessar a CNN Brasil: {response.status_code}")
            return []
        
    except Exception as e:
        print(f"Erro no scrapper da CNN: {e}")
        return []