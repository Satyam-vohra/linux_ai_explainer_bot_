# Linux AI Explainer Bot

This is a FastAPI-based bot that explains Linux commands and flags potentially dangerous ones using OpenAI's GPT API.

## Features

- Explains Linux shell commands in simple terms
- Flags dangerous or suspicious commands
- Uses a local JSON DB of known malicious patterns
- Optional HTML frontend

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint

POST /explain

```json
{
  "command": "rm -rf /"
}
```