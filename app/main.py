from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/media", response_model=schemas.MediaFile)
def read_media(title: str, db: Session = Depends(get_db)):
    # media_file = crud.get_media_file(db, title=title)
    media_file = crud.get_media_file(db, title=title)
    if media_file is None:
        raise HTTPException(status_code=404, detail="User not found")
    return media_file

@app.post("/media", response_model=schemas.MediaFile)
def write_media(media_file:schemas.MediaFileCreate, db: Session = Depends(get_db))->models.MediaFile:
    # media_file = crud.get_media_file(db, title=title)
    ret = crud.create_media_file(db, media_file)
    print(ret)
    return ret
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
