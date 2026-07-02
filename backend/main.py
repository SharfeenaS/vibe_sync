from pathlib import Path
import json

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from ai import analyze_image
from music_api import get_trending_songs
from batch_song_ai import rank_songs

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary upload folder
UPLOAD_DIR = Path("temp")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "🎵 VibeSync API is running successfully!"
    }


@app.post("/analyze")
async def analyze(
    image: UploadFile = File(...),
    languages: str = Form(...)
):

    # Convert JSON string to Python list
    selected_languages = json.loads(languages)

    image_path = UPLOAD_DIR / image.filename

    with open(image_path, "wb") as f:
        f.write(await image.read())

    try:
        # Analyze uploaded image
        image_analysis = analyze_image(str(image_path))

        # Collect songs from all selected languages
        songs = []

        for language in selected_languages:
            songs.extend(get_trending_songs(language))

        # Rank songs using AI
        recommendations = rank_songs(image_analysis, songs)

        return {
            "analysis": image_analysis,
            "recommendations": recommendations[:10]
        }

    finally:
        if image_path.exists():
            image_path.unlink()