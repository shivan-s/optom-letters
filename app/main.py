"""Main file."""
import os

import backoff
import openai
from fastapi import FastAPI
from openai.error import RateLimitError

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/")
async def root():
    """Root."""
    return {"message": "Welcome! Optom Letters"}


@backoff.on_exception(backoff.expo, RateLimitError)
@app.post("/generate_letters")
async def generate_letters(
    patient: str, optometrist: str, details: str
) -> str:
    """Generate letters."""
    # MODEL = "text-curie-001"
    MODEL = "text-davinci-003"

    details = " ".join(details.split()[:50])
    prompt = f"Write a letter to a patient, named {patient} who has {details} from an optometrist named {optometrist}"
    completion = openai.Completion.create(model=MODEL, prompt=prompt)
    return completion.choices[0].text
