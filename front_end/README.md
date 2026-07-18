# 🏆 Anime Album - Os Mais Famosos

O **Anime Album** é um álbum de figurinhas virtual e interativo que celebra os personagens mais famosos e influentes da história das animações japonesas (animes). Desde os clássicos heróis de Dragon Ball, Naruto e One Piece até ícones modernos como Demon Slayer e Jujutsu Kaisen, este projeto traz uma experiência nostálgica e interativa diretamente no navegador.

Este projeto foi desenvolvido adaptando a base da **Imersão da Alura** (Julho de 2026), focando em design moderno, interações realistas e integração com APIs.

---

## ✨ Principais Recursos

- **Virada de Página 3D Realista:** Utiliza a biblioteca `St.PageFlip` para proporcionar um efeito realista de folheamento de livro físico, permitindo arrastar páginas e folhear com suavidade e sombras dinâmicas.
- **Efeitos Sonoros Sintetizados:** Som de papel amassado e fricção gerado em tempo real via **Web Audio API** ao passar as páginas (com controle para ligar/desligar o áudio).
- **Consumo Dinâmico de API (Backend):** Os slots das figurinhas são preenchidos dinamicamente consumindo uma API FastAPI local que fornece as imagens e dados de cada personagem.
- **Navegação Inteligente:** Suporta navegação por setas laterais na interface, arraste de mouse/touch e teclas de atalho do teclado (setas esquerda e direita).
- **Design Premium & Futurista:** Fundo com gradiente radial espacial com tons de neon e azul profundo, tipografia refinada (fontes *Inter* e *Outfit*) e efeitos visuais imersivos.

---

## 📂 Categorias do Álbum

O álbum é organizado em páginas temáticas com figurinhas numeradas:

1. **Dragon Ball (Pág. 1):** Goku, Vegeta, Gohan, Piccolo e Freeza.
2. **Naruto (Pág. 2):** Naruto Uzumaki, Sasuke Uchiha, Kakashi Hatake, Itachi Uchiha e Madara Uchiha.
3. **One Piece (Pág. 3):** Monkey D. Luffy, Roronoa Zoro, Nami, Sanji e Shanks.
4. **Clássicos & Suspense (Pág. 4):** Light Yagami, L Lawliet, Edward Elric, Satoru Gojo e Killua Zoldyck.
5. **Attack on Titan / Outros (Pág. 5):** Eren Yeager, Mikasa Ackerman, Levi Ackerman, Armin Arlert e Gon Freecss.
6. **Animes Modernos (Pág. 6):** Tanjiro Kamado, Nezuko Kamado, Izuku Midoriya, Sung Jin-Woo e **Você**!

---

## 🛠️ Tecnologias Utilizadas

- **HTML5 & CSS3 (Vanilla):** Estruturação semântica e estilização customizada com gradientes, sombras e animações avançadas.
- **JavaScript (ES6+):** Lógica da aplicação, manipulação do DOM e integração de APIs.
- **Web Audio API:** Sintetizador de áudio de alta performance rodando direto no navegador para os efeitos sonoros.
- **St.PageFlip Library:** Biblioteca JavaScript de terceiros para controle de visualização do livro virtual.
- **FastAPI / Uvicorn (Backend):** Servidor Python configurado para alimentar a galeria de figurinhas de forma dinâmica na porta `8000`.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de que você possui um navegador moderno compatível com as APIs Web (Chrome, Edge, Firefox ou Safari). 

Para rodar o backend de figurinhas, é recomendável ter o **Python** instalado.

### 2. Iniciando o Backend (API)
Se você tiver o código do backend na sua máquina (ex: pasta `backend/dia-3`), execute os comandos a seguir no terminal para ligar a API:

```bash
# Entre na pasta do backend correspondente ao dia de desenvolvimento
cd backend/dia-3

# Inicie o servidor local com o Uvicorn
uvicorn main:app --reload
```
A API iniciará no endereço `http://localhost:8000` fornecendo o endpoint `/figurinhas`.

### 3. Rodando o Frontend (Álbum)
Com o backend rodando:

1. Abra a pasta `i-arq-ia-alura-album-main/` deste repositório.
2. Abra o arquivo [index.html](file:///c:/Users/Edilson%20Souza/Downloads/i-arq-ia-alura-album-main/i-arq-ia-alura-album-main/index.html) diretamente no seu navegador de preferência, ou utilize uma extensão de servidor local como o **Live Server** (do VS Code) para ter suporte completo a rotas e scripts locais.

---

## 📝 Estrutura de Arquivos

```text
i-arq-ia-alura-album-main/
│
├── i-arq-ia-alura-album-main/    # Código fonte do Frontend
│   ├── index.html                # Estrutura do Álbum e páginas
│   ├── style.css                 # Estilos visuais, efeitos e fontes
│   └── app.js                    # Inicialização do PageFlip, Áudio e Fetch API
│
└── README.md                     # Documentação do projeto (este arquivo)
```

---

Desenvolvido com 💙 para a comunidade otaku e dev. Sinta-se livre para customizar o álbum e adicionar novos personagens ou seções!
