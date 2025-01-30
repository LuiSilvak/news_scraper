from flask import Flask, render_template, jsonify
from scrapers.g1_scraper import scrape_g1
from scrapers.cnn_scraper import scrape_cnn
from scrapers.bbc_scraper import scrape_bbc
from scrapers.r7_scraper import scrape_r7
from scrapers.sbt_scraper import scrape_sbt
import json
import threading
import time

app = Flask(__name__)

# Função para carregar as notícias do arquivo JSON
def carregar_noticias():
    try:
        with open('output/noticias.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um JSON vazio
        return {"g1": [], "cnn": [], "bbc": [], "r7": [], "sbt": []}
    except json.JSONDecodeError:
        # Se o arquivo estiver corrompido, retorna um JSON vazio
        return {"g1": [], "cnn": [], "bbc": [], "r7": [], "sbt": []}

# Função para coletar e salvar notícias
def coletar_noticias():
    while True:
        todas_noticias = {
            "g1": scrape_g1(),
            "cnn": scrape_cnn(),
            "bbc": scrape_bbc(),
            "r7": scrape_r7(),
            "sbt": scrape_sbt()
        }

        #  Salvar em um arquivo JSON
        with open('output/noticias.json', 'w', encoding='utf-8') as f:
            json.dump(todas_noticias, f, ensure_ascii=False, indent=4)

        print("Notícias atualizadas!")
        time.sleep(3600)    # Atualiza a cada 1 hora

# Rota principal para exibir notícias
@app.route('/')
def index():
    noticias = carregar_noticias()
    return render_template('index.html', noticias=noticias)

# Rota para API (opcional)
@app.route('/api/noticias', methods=['GET'])
def api_noticias():
    noticias =  carregar_noticias()
    return jsonify(noticias)


if __name__ == "__main__":
    # Iniciar a coleta de notícias em uma thread separada
    threading.Thread(target=coletar_noticias, daemon=True).start()

    # Iniciar o servidor Flask
    app.run(debug=True)

