# translation_project
# API KEY (DEEPL = 5282a2ba-05f8-4d7b-a8a9-19bd6ddebf17:fx)
# translation_project

A FastAPI-based translation service with DeepL integration and custom translation logic. All translation operations are logged to a JSON file and can be viewed via an API endpoint.

---

## 🚀 How to Run This Project (VS Code)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/RoshiniPriya05/translation_project.git
   cd translation_project
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # Activate (Windows)
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install manually: `pip install fastapi uvicorn httpx python-dotenv`)*

4. **Set your DeepL API key:**
   - In PowerShell (for current session):
     ```sh
     $env:DEEPL_API_KEY="your_deepl_api_key"
     ```
   - Or, create a `.env` file in the project root:
     ```
     DEEPL_API_KEY=your_deepl_api_key
     ```

5. **Run the FastAPI server:**
   ```sh
   uvicorn main:app --reload
   ```

6. **Open the API docs:**
   - Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## 🌐 Supported Language Codes (DeepL)

| Language      | Code |
|---------------|------|
| English       | EN   |
| German        | DE   |
| French        | FR   |
| Spanish       | ES   |
| Italian       | IT   |
| Dutch         | NL   |
| Polish        | PL   |
| Portuguese    | PT   |
| Russian       | RU   |
| Japanese      | JA   |
| Chinese       | ZH   |
| Hindi         | HI   |
| ...           | ...  |

> **Full list:** [DeepL Supported Languages](https://developers.deepl.com/docs/resources/supported-languages)

---

## 📦 API Endpoints

- `/translate` (POST): Translate text (DeepL or custom logic)
- `/translate/bulk` (POST): Bulk translation (custom logic)
- `/logs` (GET): View all input/output operations

---

## 📝 View Operation Logs

All translation requests and responses are logged in `operations_log.json` in the project root.  
You can also view logs via the `/logs` endpoint in the API docs.

---

## 🔑 API Key

- **DeepL API Key:**  
  Get yours at [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api/)

---

## 👩‍💻 Author

Roshini Priya
