"""Models."""


from pydantic import BaseModel


class Optometrist(BaseModel):
    """Optometrist (i.e. sender)"""

    name: str


class Letter(BaseModel):

    content: str


class OpenAIModel(BaseModel):
    """Open AI Models."""

    id: str
    model: str
    owned_by: str
    permissions: list
