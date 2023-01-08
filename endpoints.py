search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="
song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
album_details_base_url = "https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&albumid="
playlist_details_base_url = "https://www.jiosaavn.com/api.php?__call=playlist.getDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&listid="
lyrics_base_url = "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id="
homepage_url = "https://jiosaavn.com/api.php?__call=webapi.getLaunchData&api_version=4&_format=json&_marker=0&ctx=web6dot0"
new_releases_url = "https://jiosaavn.com/api.php?__call=content.getAlbums&_format=json&cc=in&_marker=0%3F_marker%3D0"
new_releases_url_with_lang = "https://jiosaavn.com/api.php?__call=content.getAlbums&api_version=4&_format=json&_marker=0&n=50&p=1&ctx=web6dot0&languages="
charts_url = "https://jiosaavn.com/api.php?__call=content.getCharts&_format=json&cc=in&_marker=0%3F_marker%3D0"
featured_playlists_url = "https://jiosaavn.com/api.php?__call=content.getFeaturedPlaylists&_format=json&cc=in&_marker=0%3F_marker%3D0"
featured_playlists_url_with_lang = "https://jiosaavn.com//api.php?__call=content.getFeaturedPlaylists&fetch_from_serialized_files=true&p=1&n=50&api_version=4&_format=json&_marker=0&ctx=web6dot0&languages="
top_artists_url = "https://jiosaavn.com/api.php?__call=social.getTopArtists&api_version=4&_format=json&_marker=0&ctx=web6dot0"
artist_details_base_url = "https://jiosaavn.com/api.php?__call=webapi.get&type=artist&p=&n_song=50&n_album=0&sub_type=songs&category=&sort_order=&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0&token="
top_searches_url = "https://jiosaavn.com/api.php?__call=content.getTopSearches&ctx=web6dot0&api_version=4&_format=json&_marker=0"
recommendation_url = "https://jiosaavn.com/api.php?__call=reco.getAlbumReco&api_version=4&_format=json&_marker=0&ctx=web6dot0&albumid="
top_albums_url = "https://jiosaavn.com/api.php?__call=search.topAlbumsoftheYear&api_version=4&_format=json&_marker=0&ctx=web6dot0&album_year="

api_endpoints = {
    "home": "/home",
    "new_releases": "/new-releases/",
    "new_releases_with_language": "/new-releases/?lang={language}",
    "charts": "/charts/",
    "featured_playlists": "/featured-playlists/",
    "featured_playlists_with_language": "/featured-playlists/?lang={language}",
    "top_artists": "/top-artists/",
    "top_searches": "/top-searches/",
    "song_detail_by_url": "/song/?query={url}",
    "song_detail_by_id": "/song/get/?id={id}",
    "album_detail_by_url": "/album/?query={url}",
    "album_detail_by_id": "/album/get/?id={id}",
    "album_recommendations": "/album/reco/?id={album_id}",
    "top_albums_of_the_year": "/top-albums/?year={album_year}",
    "playlist_detail_by_url": "/playlist/?query={url}",
    "playlist_detail_by_id": "/playlist/get/?id={id}",
    "search": "/search/?query={search_term}",
    "lyrics": "/lyrics/?query={search_term}",
    "artist_detail": "/artist/?query={url}",
}