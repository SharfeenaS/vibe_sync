from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

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


@app.post("/analyze")
async def analyze(image: UploadFile = File(...)):

    image_path = UPLOAD_DIR / image.filename

    with open(image_path, "wb") as f:
        f.write(await image.read())

    try:

        result = analyze_image(str(image_path))

    finally:

        if image_path.exists():
            image_path.unlink()

    return result