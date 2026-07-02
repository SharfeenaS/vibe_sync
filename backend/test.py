from music_api import get_trending_songs
from song_analyzer import analyze_song

song = get_trending_songs("Malayalam")[0]

print(song)

analysis = analyze_song(song)

print(analysis)