from sqlalchemy import Column, Integer, String, Text
from settings.database_settings import Base, engine


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String)
    articles = Column(Text)

Base.metadata.create_all(bind=engine)