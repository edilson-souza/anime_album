from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceita requisições de qualquer domínio
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Define caminhos absolutos para encontrar a pasta de imagens de forma robusta
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista chamada 'figurinhas' contendo a definição das 30 figurinhas.
# As figurinhas que não possuem imagem correspondente na pasta estão comentadas.
figurinhas = [
    {"id": 1, "nome": "Goku", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Vegeta", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Gohan", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Piccolo", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Freeza", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Naruto Uzumaki", "categoria": "Naruto", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Sasuke Uchiha", "categoria": "Naruto", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Kakashi Hatake", "categoria": "Naruto", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Itachi Uchiha", "categoria": "Naruto", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Madara Uchiha", "categoria": "Naruto", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Monkey D. Luffy", "categoria": "One Piece", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Roronoa Zoro", "categoria": "One Piece", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Nami", "categoria": "One Piece", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Sanji", "categoria": "One Piece", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Shanks", "categoria": "One Piece", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Light Yagami", "categoria": "Clássicos", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "L Lawliet", "categoria": "Clássicos", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Edward Elric", "categoria": "Clássicos", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Satoru Gojo", "categoria": "Clássicos", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Killua Zoldyck", "categoria": "Clássicos", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Eren Yeager", "categoria": "Attack on Titan", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Mikasa Ackerman", "categoria": "Attack on Titan", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Levi Ackerman", "categoria": "Attack on Titan", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Armin Arlert", "categoria": "Attack on Titan", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Gon Freecss", "categoria": "Hunter x Hunter", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Tanjiro Kamado", "categoria": "Modernos", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Frien", "categoria": "Modernos", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Izuku Midoriya", "categoria": "Modernos", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Sung Jin-Woo", "categoria": "Modernos", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Edilson Souza", "categoria": "Modernos", "imagem_url": "/figurinhas/30/imagem"}
]

# Endpoint GET "/figurinhas" para retornar a lista de figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna a lista de todas as figurinhas que estão ativas no álbum.
    """
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" para buscar e retornar o arquivo físico da imagem
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    """
    Busca na pasta de imagens o arquivo com prefixo '{id:02d}[!0-9]*' usando glob.
    Retorna o arquivo de imagem se encontrado, ou gera erro 404 caso contrário.
    """
    # Cria o padrão de busca (ex: para id=1 o padrão busca arquivos começando com '01' seguidos por caractere não numérico)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Se nenhum arquivo for encontrado na pasta correspondente ao padrão, lança erro HTTP 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada para este ID")
    
    # Retorna o arquivo correspondente encontrado na pasta
    return FileResponse(arquivos[0])
