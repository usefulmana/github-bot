import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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