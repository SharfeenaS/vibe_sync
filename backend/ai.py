import json
import os

from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("Loaded key:", api_key)

client = genai.Client(api_key=api_key)


def analyze_image(image_path: str):

    image = Image.open(image_path)

    prompt = """
You are an expert visual music curator.

Analyze this image.

Return ONLY valid JSON.

{
    "mood":"",
    "aesthetic":"",
    "lighting":"",
    "scene":"",
    "dominant_colors":[],
    "emotions":[],
    "keywords":[],
    "confidence":0
}

Do not explain anything.
Do not wrap the JSON in markdown.
Return only JSON.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)