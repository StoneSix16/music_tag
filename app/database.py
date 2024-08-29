from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"{settings.db_base}{settings.db_name}"
# 用户:密码@服务器/数据库?参数
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# 会话类
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据库基类
Base = declarative_base()