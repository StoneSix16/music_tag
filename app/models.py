from sqlalchemy import Integer, Enum, Float, Uuid, DateTime, String, Text, ForeignKey, Column
import uuid, enum
from .database import Base

# class Tag(Base):
#     __tablename__ = "tag"
    
#     id = Column(Integer, primary_key=True)
#     song_id = Column(Integer, ForeignKey("song.id"))
#     tag = Column(String)

# class Song(Base):
#     __tablename__ = "song"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     artist = Column(String)

# class MediaFile(Base):
#     __tablename__ = "media_file"
    
#     id = Column(String(255), primary_key=True)
#     title = Column(String(50))
#     path = Column(String(255))
#     tag = Column(String(255))

class TagTypeEnum(enum.Enum):
    fixied = 0
    customized = 1

class PathTypeEnum(enum.Enum):
    folder = 0
    music = 1
    image = 2
    lyric = 3

class Album(Base):
    __tablename__ = "album"

    id = Column(Uuid, default=uuid.uuid4, primary_key=True)
    name = Column(String(255), index=True)
    artist = Column(ForeignKey("artist.name"), nullable=True, default='未知', index=True)
    song_count = Column(Integer, default=-1, nullable=False)
    genre = Column(ForeignKey("tag.name"), nullable=True)
    tag = Column(ForeignKey("tag.name"), nullable=True)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    accessed_at = Column(DateTime)

    comment = Column(Text, default='', nullable=True)
    description = Column(Text, default='', nullable=True)
    cover = Column(ForeignKey("cover.id"), nullable=True)
    # musicbrainz fields
    mbz_album_id = Column(String(255), nullable=True)
    mbz_album_artist_id = Column(String(255), nullable=True)
    mbz_album_type = Column(String(255), nullable=True)
    mbz_album_comment = Column(String(255), nullable=True)

    external_url = Column(String(255), default='', nullable=True)
    external_info_updated_at = Column(DateTime)

class Track(Base):
    __tablename__ = "track"

    id = Column(ForeignKey("folder.id"), primary_key=True, comment="folder id")
    name = Column(String(255), index=True)
    artist = Column(String(50), nullable=True, default='未知', index=True)
    genre = Column(ForeignKey("tag.name"), nullable=True)
    tag = Column(ForeignKey("tag.name"), nullable=True)

    path = Column(String(255))
    size = Column(Integer, default=0, nullable=True, comment="歌曲大小/Byte")
    mimetype = Column(String(255), default='', nullable=True)
    duration = Column(Float, default=0, nullable=False, comment="歌曲时长/s")
    bit_rate = Column(Integer, default=0, nullable=True)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    accessed_at = Column(DateTime)

    comment = Column(Text, default='', nullable=True)
    description = Column(Text, default='', nullable=True)
    cover = Column(ForeignKey("cover.id"), nullable=True)
    lyric = Column(ForeignKey("lyric.id"), nullable=True)
    

    # musicbrainz fields
    mbz_track_id = Column(String(255), nullable=True)
    mbz_album_id = Column(String(255), nullable=True)
    mbz_artist_id = Column(String(255), nullable=True)
    mbz_album_artist_id = Column(String(255), nullable=True)
    mbz_album_type = Column(String(255), nullable=True)
    mbz_album_comment = Column(String(255), nullable=True)

    external_url = Column(String(255), default='', nullable=True)
    external_info_updated_at = Column(DateTime)

class Artist(Base):
    __tablename__ = "artist"

    id = Column(Uuid, default=uuid.uuid4, primary_key=True)
    name = Column(String(255), index=True)
    song_count = Column(Integer, default=0, nullable=False)
    genre = Column(ForeignKey("tag.name"), nullable=True)
    tag = Column(ForeignKey("tag.name"), nullable=True)

    comment = Column(Text, default='', nullable=True)
    cover = Column(ForeignKey("cover.id"), nullable=True)

    # musicbrainz fields
    mbz_artist_id = Column(String(255), nullable=True)

    external_url = Column(String(255), default='', nullable=True)
    external_info_updated_at = Column(DateTime)


class Tag(Base):
    __tablename__ = "tag"

    name = Column(String(255), unique=True, primary_key=True)
    song_count = Column(Integer, default=0, nullable=False)
    tag_type = Column(Enum(TagTypeEnum), comment="标签类型")

class Cover(Base):
    __tablename__ = "cover"

    id = Column(ForeignKey("folder.id"), primary_key=True, comment="folder id")
    path = Column(String(255))

    # Remote URL where the image can be fetched
    url = Column(Text, nullable=True)
    size = Column(Integer, default=0, nullable=True, comment="文件大小/Byte")
    mimetype = Column(String(255), default='', nullable=True)

    created_at = Column(DateTime)
    accessed_at = Column(DateTime)

class Lyric(Base):
    __tablename__ = "lyric"

    id = Column(ForeignKey("folder.id"), primary_key=True, comment="folder id")
    path = Column(String(255))

    # Remote URL where the image can be fetched
    url = Column(Text, nullable=True)
    size = Column(Integer, default=0, nullable=True, comment="文件大小/Byte")

    created_at = Column(DateTime)
    accessed_at = Column(DateTime)

class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    created_at = Column(DateTime)
    update_at = Column(DateTime)

class Folder(Base):
    __tablename__ = "folder"

    id = Column(Uuid, default=uuid.uuid4, primary_key=True)
    parent_id = Column(Uuid, default=uuid.uuid4)
    name = Column(String(255))

    created_at = Column(DateTime)
    accessed_at = Column(DateTime)
    last_scan_at = Column(DateTime)

    # 文件类型，例如：folder, music, image，lyric
    path_type = Column(Enum(PathTypeEnum), default='folder')
    # none, scanning, scanned, updated
    state = Column(String(16), default='none')