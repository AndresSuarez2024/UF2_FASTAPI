from pydantic import BaseModel

class ThemeResponse(BaseModel):
    option: str

class WordResponse(BaseModel):
    option: str
