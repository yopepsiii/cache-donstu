from pydantic import BaseModel


class Token(BaseModel):
    email: str
    access_token: str

class TokenOut(BaseModel):
    access_token: str
    type: str