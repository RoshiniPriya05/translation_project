from fastapi import FastAPI
from app.routes import testdup_api
from app.routes import translator

app = FastAPI()

app.include_router(testdup_api.router)
app.include_router(translator.router)

@app.get("/")
def root():
    return {"message": "Hello from Udaan!"}
