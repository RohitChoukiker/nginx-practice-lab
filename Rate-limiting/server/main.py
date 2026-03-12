from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
    hostname = socket.gethostname()
    return {"message": f"Response from {hostname}"}