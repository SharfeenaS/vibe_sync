import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def rank_songs(image_analysis, songs):

    song_text = ""

    for i, song in enumerate(songs, start=1):
        song_text += f"""
{i}.
Title: {song['title']}
Artist: {song['artist']}
Popularity: {song.get('popularity', 0)}
"""

    prompt = f"""
You are an expert AI music recommender.

An image has already been analyzed.

Image Analysis:

Mood: {image_analysis["mood"]}
Aesthetic: {image_analysis["aesthetic"]}
Lighting: {image_analysis["lighting"]}
Scene: {image_analysis["scene"]}

Keywords:
{", ".join(image_analysis["keywords"])}

Emotions:
{", ".join(image_analysis["emotions"])}

Below is a list of currently trending songs.

Rank them according to how well they match the image.

Rules:
- Mood matching is MOST important.
- Then emotions.
- Then keywords.
- Then popularity.
- Higher popularity should help but should NOT override a poor mood match.

Return ONLY JSON like this:

[
  {{
    "title":"...",
    "artist":"...",
    "score":95,
    "reason":"Matches the calm natural atmosphere."
  }}
]

Songs:

{song_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)