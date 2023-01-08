import base64
import jiosaavn
from pyDes import *

def format_song(data,lyrics):
    try:
        url = data['media_preview_url']
        url = url.replace("preview", "aac")
        if data['320kbps']=="true":
            url = url.replace("_96_p.mp4", "_320.mp4")
        else:
            url = url.replace("_96_p.mp4", "_160.mp4")
        data['media_url'] = url
    except KeyError or TypeError:
        data['media_url'] = decrypt_url(data['encrypted_media_url'])
        if data['320kbps']!="true":
            data['media_url'] = data['media_url'].replace("_320.mp4","_160.mp4")

    data['song'] = format(data['song'])
    data['music'] = format(data['music'])
    data['singers'] = format(data['singers'])
    data['starring'] = format(data['starring'])
    data['album'] = format(data['album'])
    data["primary_artists"] = format(data["primary_artists"])
    data['image'] = data['image'].replace("150x150","500x500")

    if lyrics:
        if data['has_lyrics']=='true':
            data['lyrics'] = jiosaavn.get_lyrics(data['id'])
        else:
            data['lyrics'] = None

    try:
        data['copyright_text'] = data['copyright_text'].replace("&copy;","©")
    except KeyError:
        pass
    return data

def format_album(data,lyrics):
    data['image'] = data['image'].replace("150x150","500x500")
    data['name'] = format(data['name'])
    data['primary_artists'] = format(data['primary_artists'])
    data['title'] = format(data['title'])
    for song in data['songs']:
        song = format_song(song,lyrics)
    return data

def format_playlist(data,lyrics):
    data['firstname'] = format(data['firstname'])
    data['listname'] = format(data['listname'])
    for song in data['songs']:
        song = format_song(song,lyrics)
    return data

def format(string):
    return string.encode().decode('unicode-escape').replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'")

def decrypt_url(url):
    des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5)
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
    dec_url = dec_url.replace("_96.mp4", "_320.mp4")
    return dec_url

def format_home(data):
    data['new_albums'] = format_new_releases(data['new_albums'])
    for item in data['new_trending']:
        item = format_home_item(item)
    for item in data['radio']:
        item = format_home_item(item)
    for item in data['artist_recos']:
        item = format_home_item(item)
    promo_vx_data_dict = {k: v for k, v in data.items() if k.startswith('promo_vx_data_')}
    for promo in promo_vx_data_dict:
        for item in promo_vx_data_dict[promo]:
            item = format_home_item(item)
    return data

def format_home_item(data):
    data['image'] = data['image'].replace("150x150","500x500")
    data['title'] = format(data['title'])
    return data

def format_new_releases(data):
    for item in data:
        item = format_new_releases_item(item)
    return data

def format_new_releases_item(data):
    data['image'] = data['image'].replace("150x150","500x500")
    data['title'] = format(data['title'])
    return data

def format_charts(data):
    for album in data:
        album['listname'] = format(album['listname'])
        for item in album['songs']:
            item = format_charts_item(item)
    return data

def format_charts_item(data):
    data['image'] = data['image'].replace("150x150","500x500")
    data['name'] = format(data['name'])
    return data
