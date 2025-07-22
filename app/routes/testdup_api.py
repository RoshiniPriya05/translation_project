from fastapi import APIRouter
from pydantic import BaseModel
import httpx
import os
from app.utils.json_db import log_operation

router = APIRouter()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

class TranslationRequest(BaseModel):
    text: str
    target_lang: str
    source_lang: str = None  # optional

@router.post("/translate")
async def translate(req: TranslationRequest):
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "text": req.text,
        "target_lang": req.target_lang,
    }
    if req.source_lang:
        data["source_lang"] = req.source_lang

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api-free.deepl.com/v2/translate", data=data, headers=headers)

    result = response.json()
    log_operation(
        {"text": req.text, "target_lang": req.target_lang, "source_lang": req.source_lang},
        result
    )
    return result