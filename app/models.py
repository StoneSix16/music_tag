from sqlalchemy import Boolean, Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship

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

class MediaFile(Base):
    __tablename__ = "media_file"
    
    id = Column(String(255), primary_key=True)
    title = Column(String(50))
    path = Column(String(255))
    tag = Column(String(255))

# class Album(Base):
#     __tablename__ = "album"

#     id = Column('uuid', Uuid)
#     name = Column('专辑名称', String(255), )
#     artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, related_name='albums',
#                                db_constraint=False)
#     all_artist_ids = ListTextField(base_field=models.IntegerField(), default=list)

#     max_year = models.IntegerField(default=0, null=False)
#     song_count = models.IntegerField("歌曲统计", default=-1, null=False)
#     plays_count = models.IntegerField("播放次数", default=0, null=False)
#     duration = models.FloatField("歌曲时长s", default=0, null=False)
#     genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='albums', db_constraint=False)
#     created_at = models.DateTimeField(null=True)
#     updated_at = models.DateTimeField(null=True, auto_now=True)
#     accessed_date = models.DateTimeField("访问时间", null=True)

#     full_text = models.CharField(max_length=255, default='', null=True, blank=True)
#     size = models.IntegerField("文件大小", default=0, null=False)
#     comment = models.CharField(max_length=255, null=True)
#     paths = models.CharField(max_length=255, null=True)
#     description = models.CharField(max_length=255, default='', null=True)
#     attachment_cover = models.ForeignKey('Attachment', on_delete=models.SET_NULL, null=True, related_name='album_cover',
#                                          db_constraint=False)

#     # musicbrainz fields
#     mbz_album_id = models.CharField(max_length=255, null=True)
#     mbz_album_artist_id = models.CharField(max_length=255, null=True)
#     mbz_album_type = models.CharField(max_length=255, null=True)
#     mbz_album_comment = models.CharField(max_length=255, null=True)

#     external_url = models.CharField(max_length=255, default='', null=True)
#     external_info_updated_at = models.DateTimeField(null=True)

#     class Meta:
#         verbose_name = "专辑"
#         verbose_name_plural = "专辑"

#     def __str__(self):
#         return self.name


# class Track(models.Model):
#     name = models.CharField(default='', max_length=255)

#     path = models.CharField(default='', max_length=255)
#     album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, related_name='tracks', db_constraint=False)
#     artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, related_name='tracks',
#                                db_constraint=False)
#     has_cover_art = models.BooleanField(default=False)
#     track_number = models.IntegerField(default=0)
#     disc_number = models.IntegerField(default=0)
#     plays_count = models.IntegerField("播放量", default=0, null=True)
#     year = models.IntegerField(default=0, null=True)
#     size = models.IntegerField("文件大小", default=0, null=False)
#     suffix = models.CharField("后缀", default='', max_length=255, null=True)
#     mimetype = models.CharField(default='', max_length=255, null=True)
#     duration = models.FloatField("歌曲时长s", default=0, null=False)
#     bit_rate = models.IntegerField(default=0, null=True)
#     genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, related_name='tracks', db_constraint=False)
#     created_at = models.DateTimeField(null=True, auto_now_add=True)
#     updated_at = models.DateTimeField(null=True, auto_now=True)
#     accessed_date = models.DateTimeField("访问时间", null=True)
#     full_text = models.CharField(default='', max_length=255, null=True, blank=True)
#     comment = models.TextField(null=True)
#     lyrics = models.TextField(null=True)
#     # musicbrainz fields
#     mbz_track_id = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_album_id = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_artist_id = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_album_artist_id = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_album_type = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_album_comment = models.CharField(default='', max_length=255, null=True, blank=True)
#     mbz_release_track_id = models.CharField(default='', max_length=255, null=True, blank=True)

#     class Meta:
#         verbose_name = "歌曲"
#         verbose_name_plural = "歌曲"

#     def __str__(self):
#         return self.name


# class Artist(models.Model):
#     name = models.CharField(max_length=255, default='', blank=False)
#     album_count = models.IntegerField(default=0)
#     full_text = models.CharField(max_length=255, default='', null=True, blank=True)

#     song_count = models.IntegerField(default=0, null=True, blank=True)
#     size = models.IntegerField(default=0, null=True, blank=True)
#     mbz_artist_id = models.CharField(max_length=255, null=True, blank=True)
#     attachment_cover = models.ForeignKey('Attachment', null=True, blank=True, on_delete=models.SET_NULL,
#                                          related_name='artist_cover')

#     similar_artists = models.CharField(max_length=255, default='', null=True, blank=True)
#     external_url = models.CharField(max_length=255, default='', null=True, blank=True)
#     external_info_updated_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         verbose_name = "艺术家"
#         verbose_name_plural = "艺术家"

#     def __str__(self):
#         return self.name


# class Genre(models.Model):
#     name = models.CharField(max_length=255, unique=True)

#     class Meta:
#         verbose_name = "风格"
#         verbose_name_plural = "风格"