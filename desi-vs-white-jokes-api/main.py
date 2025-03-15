from jokes import desi_jokes, white_jokes
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/white_jokes")
def get_white_jokes():
    """Returns a random white joke"""
    return random.choice(white_jokes)

@app.get("/desi_jokes")
def get_desi_jokes():
    """Returns a random desi joke"""
    return random.choice(desi_jokes)


