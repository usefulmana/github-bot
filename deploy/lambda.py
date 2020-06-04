import os
import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Text, DateTime
import requests
from datetime import datetime

load_dotenv()
# Load Env Vars
db_string = os.getenv('DB_STRING')
token = os.getenv('AUTH_TOKEN')
url = os.getenv('GITHUB_URL')

# DB Connection
db = sqlalchemy.create_engine(db_string)
Base = declarative_base()
Session = sessionmaker(bind=db)
# create a Session
session = Session()


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


def get_repos():
    res = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    return res.json()


def parse_response(res):
    for item in res:
        updated_at = datetime.strptime(
            item.get('updated_at'), '%Y-%m-%dT%H:%M:%SZ')
        repo = Repo(item.get('name'), item.get('html_url'), item.get('description'),
                    updated_at, item.get('stargazers_count'), item.get('watchers_count'))
        session.add(repo)
    session.commit()
    session.close()


def initialize_database():
    if db.dialect.has_table(db, Repo.__tablename__):
        # Drop Table if exist
        Repo.__table__.drop(db)
    # Recreate Table
    Repo.metadata.create_all(db)


def run():
    initialize_database()
    parse_response(get_repos())
    print("Done!")

def lambda_handler(event='', context=''):
    what_to_print = os.environ.get("GITHUB_URL")
    if what_to_print:
        run()
        return {
            'statusCode': 200,
            'body': json.dumps(what_to_print)
        }
    return {
        'statusCode': 500,
        'body': json.dumps("Failed!")
    }


if __name__ == '__main__':
    lambda_handler()
