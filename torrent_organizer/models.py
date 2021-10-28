from pydantic import BaseModel


class MediaFile(BaseModel):
    name: str
    path: str
