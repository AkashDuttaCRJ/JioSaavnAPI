from flask import Flask, request, redirect, jsonify, json
import time

import requests
import jiosaavn
import os
from traceback import print_exc
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET",'thankyoutonystark#weloveyou3000')
CORS(app)


@app.route('/home')
def home():
    return jsonify(jiosaavn.get_home())

@app.route('/new-releases/')
def new_releases():
    lang = request.args.get('lang')
    if lang is None:
        lang = False
    return jsonify(jiosaavn.get_new_releases_with_lang(lang) if lang else jiosaavn.get_new_releases())

@app.route('/charts/')
def charts():
    return jsonify(jiosaavn.get_charts())

@app.route('/featured-playlists/')
def featured_playlists():
    lang = request.args.get('lang')
    if lang is None:
        lang = False
    return jsonify(jiosaavn.get_featured_playlists(lang))

@app.route('/top-artists/')
def top_artists():
    return jsonify(jiosaavn.get_top_artists())

@app.route('/artist/')
def artist():
    query = request.args.get('query')
    return jsonify(jiosaavn.get_artist_detail(query))

@app.route('/top-searches/')
def top_searches():
    return jsonify(jiosaavn.get_top_searches())

@app.route('/top-albums/')
def top_albums():
    year = request.args.get('year')
    return jsonify(jiosaavn.get_top_albums(year))

@app.route('/song/')
def search():
    lyrics = False
    query = request.args.get('query')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        id = jiosaavn.get_song_id(query)
        return jsonify(jiosaavn.get_song(id, lyrics))
    else:
        error = {
            "status": False,
            "error":'Query is required to search songs!'
        }
        return jsonify(error)

@app.route('/song/get/')
def get_song():
    lyrics = False
    id = request.args.get('id')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if id:
        resp = jiosaavn.get_song(id,lyrics)
        if not resp:
            error = {
                "status": False,
                "error": 'Invalid Song ID received!'
            }
            return jsonify(error)
        else:
            return jsonify(resp)
    else:
        error = {
            "status": False,
            "error": 'Song ID is required to get a song!'
        }
        return jsonify(error)

@app.route('/playlist/')
def playlist():
    lyrics = False
    query = request.args.get('query')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        id = jiosaavn.get_playlist_id(query)
        songs = jiosaavn.get_playlist(id,lyrics)
        return jsonify(songs)
    else:
        error = {
            "status": False,
            "error":'Query is required to search playlists!'
        }
        return jsonify(error)

@app.route('/playlist/get/')
def get_playlist():
    lyrics = False
    id = request.args.get('id')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if id:
        resp = jiosaavn.get_playlist(id,lyrics)
        if not resp:
            error = {
                "status": False,
                "error": 'Invalid Playlist ID received!'
            }
            return jsonify(error)
        else:
            return jsonify(resp)
    else:
        error = {
            "status": False,
            "error": 'Playlist ID is required to get a playlist!'
        }
        return jsonify(error)

@app.route('/album/')
def album():
    lyrics = False
    query = request.args.get('query')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        id = jiosaavn.get_album_id(query)
        songs = jiosaavn.get_album(id,lyrics)
        return jsonify(songs)
    else:
        error = {
            "status": False,
            "error":'Query is required to search albums!'
        }
        return jsonify(error)

@app.route('/album/get/')
def get_album():
    lyrics = False
    id = request.args.get('id')
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if id:
        resp = jiosaavn.get_album(id,lyrics)
        if not resp:
            error = {
                "status": False,
                "error": 'Invalid Album ID received!'
            }
            return jsonify(error)
        else:
            return jsonify(resp)
    else:
        error = {
            "status": False,
            "error": 'Album ID is required to get a album!'
        }
        return jsonify(error)

@app.route('/album/reco/')
def recommendations():
    id = request.args.get('id')
    return jsonify(jiosaavn.get_recommendations(id))

@app.route('/lyrics/')
def lyrics():
    query = request.args.get('query')

    if query:
        try:
            if 'http' in query and 'saavn' in query:
                id = jiosaavn.get_song_id(query)
                lyrics = jiosaavn.get_lyrics(id)
            else:
                lyrics = jiosaavn.get_lyrics(query)
            response = {}
            response['status'] = True
            response['lyrics'] = lyrics
            return jsonify(response)
        except Exception as e:
            error = {
            "status": False,
            "error": str(e)
            }
            return jsonify(error)
        
    else:
        error = {
            "status": False,
            "error":'Query containing song link or id is required to fetch lyrics!'
        }
        return jsonify(error)


@app.route('/search/')
def result():
    query = request.args.get('query')
    return jsonify(jiosaavn.search(query))

@app.route('/endpoints/')
def endpoints():
    return jsonify(jiosaavn.get_endpoints())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5100, use_reloader=True, threaded=True)
