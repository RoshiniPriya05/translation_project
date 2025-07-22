from fastapi import FastAPI
from app.routes import testdup_api  # Make sure 'app' is a package (has __init__.py)

app = FastAPI()

app.include_router(testdup_api.router)

@app.get("/")
def root():
    return {"message": "Hello from Udaan!"}