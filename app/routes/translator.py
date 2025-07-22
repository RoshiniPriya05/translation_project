from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from app.services.translate_service import translate_text
from app.utils.logger import log_request

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

class BulkTranslationRequest(BaseModel):
    texts: List[str]
    target_lang: str

@router.post("/translate")
def translate_single(request: TranslationRequest):
    if len(request.text) > 1000:
        raise HTTPException(status_code=400, detail="Text exceeds 1000 characters.")
    translated = translate_text(request.text, request.target_lang)
    log_request(request.text, request.target_lang)
    return {"translated_text": translated}

@router.post("/translate/bulk")
def translate_bulk(request: BulkTranslationRequest):
    results = [translate_text(text, request.target_lang) for text in request.texts]
    for text in request.texts:
        log_request(text, request.target_lang)
    return {"results": results}

