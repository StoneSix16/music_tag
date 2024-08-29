from sqlalchemy.orm import Session
import uuid
from . import schemas, models

def get_album_by_name(db: Session, name: str):
    return db.query(models.Album).filter(models.Album.name == name).first()

def create_album(db: Session, album: schemas.AlbumCreate):
    db_Album = models.Album
    new_album = db_Album(name=album.name,
                             tag='H')
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album

# NOTE :
# - add that instance object to your database session.
# - commit the changes to the database (so that they are saved).
# - refresh your instance (so that it contains any new data from the database, like the generated ID).