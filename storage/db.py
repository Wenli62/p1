from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

user = app_config['datastore']['user']
password = app_config['datastore']['password']
hostname = app_config['datastore']['hostname']
port = app_config['datastore']['port']
db = app_config['datastore']['db']

engine = create_engine(f"mysql://{user}:{password}@{hostname}:{port}/{db}")

def make_session():
    return sessionmaker(bind=engine)()