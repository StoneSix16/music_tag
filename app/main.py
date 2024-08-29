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


@app.get("/media", response_model=schemas.Album)
def read_album(name: str, db: Session = Depends(get_db)):
    # media_file = crud.get_media_file(db, title=title)
    media_file = crud.create_album(db, name=name)
    if media_file is None:
        raise HTTPException(status_code=404, detail="User not found")
    return media_file

@app.post("/media", response_model=schemas.Album)
def write_album(media_file:schemas.AlbumCreate, db: Session = Depends(get_db))->models.Album:
    # media_file = crud.get_media_file(db, title=title)
    ret = crud.create_album(db, media_file)
    return ret
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
