import requests
import endpoints
import helper
import json
from traceback import print_exc

def search(query):
    search_url = endpoints.search_base_url+query
    search_response = requests.get(search_url).text.encode().decode('unicode-escape')
    search_data = json.loads(search_response)
    return search_data

def get_song(id,lyrics):
    try:
        song_details_base_url = endpoints.song_details_base_url+id
        song_response = requests.get(song_details_base_url).text.encode().decode('unicode-escape')
        song_response = json.loads(song_response)
        song_data = helper.format_song(song_response[id],lyrics)
        if song_data:
            return song_data
    except:
        return None

def get_song_id(url):
    res = requests.get(url, data=[('bitrate', '320')])
    try:
        return res.text.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
    except IndexError:
        return(res.text.split('"pid":"'))[1].split('","')[0]

def get_album(album_id,lyrics):
    songs_json = []
    try:
        response = requests.get(endpoints.album_details_base_url+album_id)
        if response.status_code == 200:
            songs_json = response.text.encode().decode('unicode-escape')
            songs_json = json.loads(songs_json)
            return helper.format_album(songs_json,lyrics)
    except Exception as e:
        print(e)
        return None

def get_album_id(input_url):
    res = requests.get(input_url)
    try:
        return res.text.split('"album_id":"')[1].split('"')[0]
    except IndexError:
        return res.text.split('"page_id","')[1].split('","')[0]

def get_playlist(listId,lyrics):
    try:
        response = requests.get(endpoints.playlist_details_base_url+listId)
        if response.status_code == 200:
            songs_json = response.text.encode().decode('unicode-escape')
            songs_json = json.loads(songs_json)
            return helper.format_playlist(songs_json,lyrics)
        return None
    except Exception:
        print_exc()
        return None

def get_playlist_id(input_url):
    res = requests.get(input_url).text
    try:
        return res.split('"type":"playlist","id":"')[1].split('"')[0]
    except IndexError:
        return res.split('"page_id","')[1].split('","')[0]

def get_lyrics(id):
    url = endpoints.lyrics_base_url+id
    lyrics_json = requests.get(url).text
    lyrics_text = json.loads(lyrics_json)
    return lyrics_text['lyrics']

def get_home():
    url = endpoints.homepage_url
    homepage_json = requests.get(url).text
    homepage_text = json.loads(homepage_json)
    return helper.format_home(homepage_text)

def get_new_releases():
    url = endpoints.new_releases_url
    new_releases_json = requests.get(url).text
    new_releases_text = json.loads(new_releases_json)
    return helper.format_new_releases(new_releases_text)

def get_new_releases_with_lang(lang):
    url = endpoints.new_releases_url_with_lang+lang
    new_releases_json = requests.get(url).text
    new_releases_text = json.loads(new_releases_json)
    return new_releases_text

def get_charts():
    url = endpoints.charts_url
    charts_json = requests.get(url).text
    charts_text = json.loads(charts_json)
    return helper.format_charts(charts_text)

def get_featured_playlists(lang):
    url = endpoints.featured_playlists_url_with_lang+lang if lang else endpoints.featured_playlists_url
    featured_playlists_json = requests.get(url).text
    featured_playlists_text = json.loads(featured_playlists_json)
    return featured_playlists_text

def get_top_artists():
    url = endpoints.top_artists_url
    top_artists_json = requests.get(url).text
    top_artists_text = json.loads(top_artists_json)
    return top_artists_text

def get_artist_detail(query):
    url_components = query.split("/")
    artist_url = endpoints.artist_details_base_url+url_components[-1]
    artist_details_response = requests.get(artist_url).text
    artist_details_text = json.loads(artist_details_response)
    artist_details_text['bio'] = ''
    return artist_details_text

def get_top_searches():
    top_search_url = endpoints.top_searches_url
    top_search_response = requests.get(top_search_url).text
    top_search_text = json.loads(top_search_response)
    return top_search_text