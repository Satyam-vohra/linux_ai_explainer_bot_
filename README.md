# 🧠 Linux AI Command Explainer Bot

A powerful FastAPI-based tool that explains any Linux command using OpenAI and also checks for potentially dangerous commands like `rm -rf /`.

![Demo](https://img.shields.io/badge/status-active-brightgreen)
![Built With](https://img.shields.io/badge/built%20with-FastAPI-blue)
![License](https://img.shields.io/github/license/Satyam-vohra/linux_ai_explainer_bot)

---


## 🚀 Features

- 🧾 **AI Explanation** of any Linux command using GPT-3.5/4
- ⚠️ **Suspicious Command Detection** from custom JSON list
- 🧪 **Interactive API Testing** using Swagger UI
- 🧰 **Simple & Clean Code** with `.env` support
- 🌐 **Frontend ready**: Connects easily with an HTML UI

---

## 📁 Project Structure

linux_ai_explainer_bot/
├── main.py # FastAPI backend logic
├── threats.json # Suspicious command patterns
├── .env # OpenAI API key (not uploaded)
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Satyam-vohra/linux_ai_explainer_bot.git
cd linux_ai_explainer_bot
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Add OpenAI API Key
Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
4. Run the Server
bash
Copy
Edit
python -m uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs to use Swagger UI.

📡 API Endpoint
POST /explain

🔸 Request:
json
Copy
Edit
{
  "command": "rm -rf /"
}
🔸 Response:
json
Copy
Edit
{
  "command": "rm -rf /",
  "explanation": "This command forcefully deletes all files from the root directory...",
  "safety": {
    "status": "suspicious",
    "reason": "Deletes all files in the root directory"
  }
}
📃 License
This project is licensed under the MIT License.

💡 Feedback & Contributions
Feel free to raise issues or suggest new features.
Pull requests are welcome!

📌 Tags
#FastAPI #LinuxCommands #OpenAI #CyberSecurity #Python #AI #API

yaml
Copy
Edit

---

### ✅ Kaise Use Karna Hai?

1. **Create a file** named `README.md` in your project folder.
2. Paste above content in it.
3. Save & commit it:

```bash
git add README.md
git commit -m "Added project README"
git push
