"""Models."""


from pydantic import BaseModel


class ResponseModel(BaseModel):
    patient: str
    optometrist: str
    contents: str
