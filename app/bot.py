import requests
from app.models import Repo
from app import url, token, db, session
from datetime import datetime


def get_repos():
    res = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    return res.json()


def parse_response(res):
    for item in res:
        updated_at = datetime.strptime(item.get('updated_at'), '%Y-%m-%dT%H:%M:%SZ')
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


if __name__ == '__main__':
    initialize_database()
    parse_response(get_repos())
    print("Done!")

