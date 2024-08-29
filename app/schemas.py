from models import TagTypeEnum, PathTypeEnum
from pydantic import BaseModel

class AlbumCreate(BaseModel):
    name: str
    artist: str|None = None

    song_count: int = 0
    genre: list[str]|None = None
    tag: list[str]|None = None
    comment: str|None = None
    description: str|None = None
    cover: list[str]|None = None

    # musicbrainz fields
    mbz_album_id: str|None = None
    mbz_album_artist_id: str|None = None
    mbz_album_type: str|None = None
    mbz_album_comment: str|None = None

    external_url: str|None = None
    external_info_updated_at: str|None = None
    
class Album(AlbumCreate):
    id: str
    create_at: str
    updated_at: str
    accessed_at: str

    class Config:
        orm_mode = True

class TrackCreate(BaseModel):
    name: str
    artist: str|None = None
    genre: str|None = None
    tag: str|None = None

    path: str
    size: int|None = None
    mimetype: str|None = None
    duration: float|None = None
    bit_rate: int|None = None



    comment: str|None = None
    description: str|None = None
    cover: str|None = None

    # musicbrainz fields
    mbz_track_id: str|None = None
    mbz_album_id: str|None = None
    mbz_artist_id: str|None = None
    mbz_album_artist_id: str|None = None
    mbz_album_type: str|None = None
    mbz_album_comment: str|None = None

    external_url: str|None = None
    external_info_updated_at: str|None = None

class Track(TrackCreate):
    id: str
    created_at: str
    updated_at: str
    accessed_at: str

    class Config:
        orm_mode = True

class ArtistCreate(BaseModel):
    name: str
    genre: str|None = None
    tag: str|None = None

    comment: str|None = None
    cover: str|None = None

    # musicbrainz fields
    mbz_artist_id: str|None = None

    external_url: str|None = None
    external_info_updated_at: str|None = None

class Artist(ArtistCreate):
    id: str
    song_count: int

    class Config:
        orm_mode = True

class TagCreate(BaseModel):
    name: str
    tag_type: TagTypeEnum

class Tag(TagCreate):
    class Config:
        orm_mode = True

class CoverCreate(BaseModel):
    path: str
    url: str|None = None
    size: int|None = None
    mimetype: str|None = None

class Cover(CoverCreate):
    id: str
    created_at: str
    accessed_at: str

    class Config:
        orm_mode = True

class LyricCreate(BaseModel):
    path: str
    url: str|None = None
    size: int|None = None

class Lyric(LyricCreate):
    id: str
    created_at: str
    accessed_at: str

    class Config:
        orm_mode = True

class PlaylistCreate(BaseModel):
    name: str

class Playlist(PlaylistCreate):
    id: str
    created_at: str
    update_at: str

    class Config:
        orm_mode = True

class FolderCreate(BaseModel):
    name: str
    path_type: PathTypeEnum

class Folder(FolderCreate):
    id: str
    parent_id: str
    created_at: str
    update_at: str
    last_scan_at: str
    state: str

    class Config:
        orm_mode = True
