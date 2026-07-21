import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "Hello from server!"}

# Add this entrypoint function
def run():
  uvicorn.run("app.server:app", host="127.0.0.1", port=8000, reload=True)