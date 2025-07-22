# app/services/translate_service.py

translations = {
    "hello": {
        "ta": "வணக்கம்",
        "hi": "नमस्ते",
        "kn": "ಹೆಲೋ",
        "bn": "হ্যালো"
    }
}

def translate_text(text, target_lang):
    word = text.strip().lower()
    if word in translations and target_lang in translations[word]:
        return translations[word][target_lang]
    return f"[Translated '{text}' to '{target_lang}']"
