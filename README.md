# YouTube Playlist Creator

Este projeto permite criar playlists no YouTube a partir de playlists do Spotify. Ele autentica no Spotify para obter as músicas e depois pesquisa os vídeos correspondentes no YouTube, adicionando-os a uma playlist.

## 🚀 Funcionalidades
- Autenticação na API do Spotify
- Busca de músicas em uma playlist do Spotify
- Pesquisa automática dos vídeos correspondentes no YouTube
- Adição dos vídeos em uma playlist específica no YouTube

## 🛠️ Tecnologias Utilizadas
- Python
- Requests
- Google API Client (YouTube Data API v3)
- OAuth 2.0
- dotenv

## 📦 Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Entre no diretório do projeto:
   ```sh
   cd nome-do-projeto
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## 🔑 Configuração das Credenciais
1. Crie suas credenciais no Spotify e YouTube:
   - Spotify: [Link](https://developer.spotify.com/dashboard)
   - YouTube: [Link](https://console.cloud.google.com/)
2. No arquivo `.env` no diretório raiz, adicione suas credenciais do Spotify e YouTube:
   ```env
   CLIENT_ID=seu_client_id_spotify
   CLIENT_SECRET=seu_client_secret_spotify
   YOUTUBE_KEY=seu_youtube_api_key
   ```
3. Baixe o arquivo JSON de credenciais do Google e coloque-o na pasta do projeto.

4. Na linha 13 do código, substitua a URL pela playlist do Spotify que deseja copiar para o YouTube:
   ```sh
   url_playlist = 'https://open.spotify.com/playlist/ID_DA_PLAYLIST' 
   ```

5. Crie uma playlist na conta do Google para a qual gerou as credenciais de acesso. Copie o ID da playlist criada e substitua no código:
   ```sh
   playlist_id = 'ID_DE_SUA_PLAYLIST'  
   ```

## ▶️ Uso
Execute o script principal:
```sh
python main.py
```
