from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from settings.database_settings import Base, engine


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String)
    articles = Column(Text)
    table_args = (UniqueConstraint('title', name='unique_news_title'))

Base.metadata.create_all(bind=engine)