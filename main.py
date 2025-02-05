import requests
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from dotenv import load_dotenv

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
load_dotenv(".env") 

url_playlist = 'https://open.spotify.com/playlist/ID_DA_PLAYLIST'
playlist_id = 'ID_DE_SUA_PLAYLIST'
youtube_id_videos = []
list_music = [] 
SPOTIFY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_KEY')


def spotify_auth():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        token_info = response.json()
        token = token_info['access_token']
        return token
    else:
        print(f"Error: {response.status_code, response.text}")
        return None

def get_tracks(list_music, ACCESS_TOKEN, url_playlist):
    if not ACCESS_TOKEN:
        print("Token nao encontrado. Verifique as credenciais do Spotify.")
        return None
    try:
        playlist_id = url_playlist.split('playlist/')[1].split('/')[0]
        if not playlist_id or len(playlist_id) != 22:
            raise ValueError(f"Playlist ID invalido: {playlist_id}")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
    url_playlist_api = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    headers = {
        "Authorization" : f"Bearer {ACCESS_TOKEN}"
    }
    try:
        response = requests.get(url_playlist_api, headers=headers)
        if response.status_code == 200:
            tracks = response.json()['items']

            for item in tracks:
                music_name = item['track']
                artists_name = music_name['artists']
                list_music.append(music_name['name'] + ' - ' + artists_name[0]['name'])
            print("Musicas: {list_music}")
        else:
            print("Error: {response.status_code, response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def scraping_youtube(list_music, youtube_id_videos): 
    rows = 0
    while rows < len(list_music):
        youtube_search = 'https://www.youtube.com/results?search_query='+ list_music[rows]

        response = requests.get(youtube_search)
    
        find_id = response.text.split('videoId":"')[1].split('"')[0]
        print(find_id)
        rows += 1
        youtube_id_videos.append(find_id)
    rows = 0
    print(f"Youtube ID: {youtube_id_videos}")

def youtube_credetials():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'CLIENT_SECRET_YOUTUBEV3_API.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def youtube_api_insert(playlist_id, videos):
        
    request = youtube.playlistItems().insert(
        part='snippet',
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": videos
                }
            }
        }
    )
    try:
        response = request.execute()
        return response
    except HttpError as e:
        print(f"Erro: {e}")
        return None

def execute_youtube_api(youtube_id_videos):
    for videos in youtube_id_videos:
        youtube_api_insert(playlist_id, videos)
        print(f"Video: {videos} adicionado na playlist!")

ACCESS_TOKEN = spotify_auth()
get_tracks(list_music, url_playlist)
scraping_youtube(list_music, youtube_id_videos)
creds = youtube_credetials()
youtube = build('youtube', 'v3', credentials=creds)
execute_youtube_api(youtube_id_videos)