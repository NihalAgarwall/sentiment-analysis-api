# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import pipeline

# --- 1. Load the AI Model ---
sentiment_analyzer = pipeline(
    task="sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# --- 2. Define the Request Body Data Structure ---
class TextToAnalyze(BaseModel):
    text: str

# --- 3. Create the FastAPI App Instance ---
app = FastAPI(
    title="Sentiment Analysis API",
    description="An API to analyze text sentiment using a DistilBERT model.",
    version="0.1.0",
)

# --- 4. Mount the Static Files Directory ---
# This line tells FastAPI to serve all files from the 'static' directory
# under the path '/static'.
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# --- 5. Define API Endpoints ---
@app.get("/")
async def read_root():
    """
    Serve the main index.html file for the frontend.
    """
    return FileResponse('app/static/index.html')


@app.post("/analyze/")
async def analyze_sentiment(request_data: TextToAnalyze):
    """
    Analyzes the sentiment of the text provided in the request.
    Returns the sentiment label and a confidence score.
    """
    result = sentiment_analyzer(request_data.text)
    return result[0]