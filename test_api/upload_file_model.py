from pydantic import BaseModel


class UploadModel(BaseModel):
    code: int
    type: str
    message: str
