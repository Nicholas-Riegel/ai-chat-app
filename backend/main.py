from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change '*' to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):

    data = await request.json()
    input = data.get("input")

    if not input:
        return Response(
            content='{"error": "Input is required"}', 
            media_type="application/json", 
            status_code=400
        )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "prompt": input,
            "stream": False,
            "model": "llama3.2"
        }
    )

    return Response(
        content=response.text,
        media_type="application/json"
    )