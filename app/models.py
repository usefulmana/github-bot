from app import Base
from sqlalchemy import Column, Integer, String, Text, DateTime


class Repo(Base):
    __tablename__ = 'repos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    html_url = Column(String(100), nullable=False)
    description = Column(Text)
    updated_at = Column(DateTime, nullable=False)
    stars = Column(Integer, nullable=False)
    watchers = Column(Integer, nullable=False)

    def __init__(self, name, url, desc, updated_at, stars, watchers):
        self.name = name
        self.html_url = url
        self.description = desc
        self.updated_at = updated_at
        self.stars = stars
        self.watchers = watchers

    def __repr__(self):
        return f"<Repo(name={self.name}, updated_at={self.updated_at.strftime('%Y-%m-%d')})>"
