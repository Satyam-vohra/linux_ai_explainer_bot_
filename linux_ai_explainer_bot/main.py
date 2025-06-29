from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import json
import os
from dotenv import load_dotenv

# Load .env file (for OpenAI API key)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load from .env

app = FastAPI()

# ✅ Enable CORS for frontend HTML/JS fetch to work
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for local testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load suspicious commands from threats.json
with open("threats.json") as f:
    threat_data = json.load(f)["suspicious_patterns"]

# Check if the command matches any suspicious pattern
def check_suspicious(command):
    for item in threat_data:
        if item["command"] in command:
            return {"status": "suspicious", "reason": item["reason"]}
    return {"status": "safe", "reason": "No known threats found"}

# Generate explanation using OpenAI
def explain_command(command):
    try:
        prompt = f"Explain this Linux command in simple terms: `{command}`"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error from OpenAI: {str(e)}"

# API endpoint
@app.post("/explain")
async def explain(request: Request):
    try:
        data = await request.json()
        command = data.get("command", "")
        if not command:
            return {"error": "No command provided"}
        explanation = explain_command(command)
        safety = check_suspicious(command)
        return {
            "command": command,
            "explanation": explanation,
            "safety": safety
        }
    except Exception as e:
        return {"error": f"Invalid request: {str(e)}"}
