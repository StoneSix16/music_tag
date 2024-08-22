from pydantic import BaseModel

class MediaFileBase(BaseModel):
    title: str
    path: str
    id: str

class MediaFileCreate(MediaFileBase):
    pass

class MediaFile(MediaFileBase):
    tag: str
    class Config:
        orm_mode = True

