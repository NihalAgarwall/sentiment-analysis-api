# AI-Powered Sentiment Analysis API

A full-stack web application that analyzes the sentiment of a piece of text using a pre-trained AI model from Hugging Face. The project is built with FastAPI on the backend and vanilla HTML/CSS/JS on the frontend.

## Features
-   Analyzes text for **POSITIVE** or **NEGATIVE** sentiment.
-   Displays the model's confidence score.
-   RESTful API backend.
-   Simple, responsive user interface.

## Tech Stack
-   **Backend:** Python, FastAPI
-   **AI/ML:** Hugging Face Transformers, PyTorch
-   **Frontend:** HTML, CSS, JavaScript

## How to Run Locally

1.  Clone the repository.
2.  Create and activate a Python virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the server:
    ```bash
    uvicorn app.main:app --reload
    ```
5.  Open your browser to `http://127.0.0.1:8000`.