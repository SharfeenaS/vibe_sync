from pathlib import Path
from music_api import get_trending_songs
from ranking import recommend_songs
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from batch_song_ai import rank_songs
from ai import analyze_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("temp")
UPLOAD_DIR.mkdir(exist_ok=True)


from fastapi import Form
import json

@app.post("/analyze")
async def analyze(
    image: UploadFile = File(...),
    languages: str = Form(...)
):

    image_path = UPLOAD_DIR / image.filename

    with open(image_path, "wb") as f:
        f.write(await image.read())

    try:

        result = analyze_image(str(image_path))

        songs = []

        for language in selected_languages:
            songs.extend(get_trending_songs(language))

# Let AI understand every song
        recommendations = rank_songs(result, songs)

    finally:

        if image_path.exists():
            image_path.unlink()

    return {
    "analysis": result,
    "recommendations": recommendations[:10]
}