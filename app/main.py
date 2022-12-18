"""Main file."""
import os
import re
from enum import Enum

import backoff
import openai
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from jinja2 import pass_eval_context
from markupsafe import Markup
from openai.error import RateLimitError

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@pass_eval_context
def nl2br(eval_ctx, value):
    br = "<br>\n"

    if eval_ctx.autoescape:
        br = Markup(br)

    result = "\n\n".join(
        f"<p>{br.join(p.splitlines())}</p>"
        for p in re.split(r"(?:\r\n|\r(?!\n)|\n){2,}", value)
    )
    return Markup(result)


templates.env.filters["nl2br"] = nl2br


class AddressedTo(Enum):
    GP: str = "General Practitioner"
    SPECIALIST: str = "Specialist"
    PATIENT: str = "Patient"


@app.get("/")
async def index(request: Request):
    """Root."""
    return templates.TemplateResponse(
        "index.html", {"request": request, "options": AddressedTo}
    )


@backoff.on_exception(backoff.expo, RateLimitError)
@app.post("/generate_letter")
async def generate_letters(
    request: Request,
    patient: str = Form(),
    addressed_to: str = Form(),
    optometrist: str = Form(),
    contents: str = Form(),
):
    """Endpoint to generate letters."""
    model = "text-curie-001"
    # model = "text-davinci-003"

    prompt_lookup = {
        AddressedTo.GP.value: f"an eye report to a general practice doctor about",
        AddressedTo.SPECIALIST.value: f"a referral letter to a specialist about",
        AddressedTo.PATIENT.value: f"an eye report addressed",
    }
    prompt = f"Write {prompt_lookup[addressed_to]} a patient, named {patient[:25]} signed by an optometrist, named {optometrist[:25]}"

    max_tokens = 2024 - len(prompt.split())
    completion = openai.Completion.create(
        model=model, prompt=prompt, max_tokens=max_tokens
    )
    return templates.TemplateResponse(
        "partials/response.html",
        {
            "request": request,
            "response": completion.choices[0].text,
        },
    )
