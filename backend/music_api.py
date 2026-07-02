import requests


def get_trending_songs(language):

    queries = {
        "Malayalam": "Malayalam",
        "Tamil": "Tamil",
        "Hindi": "Hindi",
        "English": "English",
        "Korean": "K-Pop",
        "Japanese": "J-Pop"
    }

    search = queries.get(language, language)

    url = "https://itunes.apple.com/search"

    params = {
        "term": search,
        "entity": "song",
        "limit": 25
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    songs = []

    for item in data.get("results", []):

        songs.append({

            "title": item.get("trackName", ""),

            "artist": item.get("artistName", ""),

            "language": language,

            "mood": "",

            "keywords": [],

            # Placeholder until we build popularity scoring
            "popularity": 70

        })

    return songs