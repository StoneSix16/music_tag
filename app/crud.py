from sqlalchemy.orm import Session
from .models import MediaFile
from . import schemas

def get_media_file(db: Session, title: str):
    return db.query(MediaFile).filter(MediaFile.title == title).first()

def create_media_file(db: Session, media_file: schemas.MediaFileCreate):
    db_media_file = MediaFile(title=media_file.title,
                              path=media_file.path,
                              id=media_file.id,
                              tag='None')
    db.add(db_media_file)
    db.commit()
    db.refresh(db_media_file)
    return db_media_file

# NOTE :
# - add that instance object to your database session.
# - commit the changes to the database (so that they are saved).
# - refresh your instance (so that it contains any new data from the database, like the generated ID).