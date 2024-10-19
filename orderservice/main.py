from fastapi import FastAPI

from orderservice.db import lifespan

app = FastAPI(lifespan=lifespan)

@app.get('/')
def test_root():
    return {"hello":"world"}

