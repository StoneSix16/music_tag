from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "music_tag"
    db_base: str = "mysql+pymysql://root:123456@localhost:3306/"
    db_name: str = "musictag"

    class Config:
        env_file = ".env"