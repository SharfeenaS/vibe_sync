from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # We'll restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to VibeSync API 🚀"}

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "message": "Image received successfully!"
    }