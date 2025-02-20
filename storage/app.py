import connexion
import logging
import logging.config
import yaml
import functools
from db import make_session
from models import gradeReport
import yaml
import logging, logging.config
import jwt


with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open("log_conf.yml", "r") as f:
    LOG_CONFIG = yaml.safe_load(f.read())
    logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger('basicLogger')

app = connexion.FlaskApp(__name__, specification_dir='')

app.add_api("mysql.yaml", strict_validation=True, validate_responses=True)

def load_yaml(file, default={}):
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return default

SECRET_KEY = app_config["secret_key"]


def validate_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None 
    except jwt.InvalidTokenError:
        return None

def use_db_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = make_session()
        try:
            event = func(session, *args, **kwargs)
            session.add(event)
            session.commit()
        finally:
            session.close()
    return wrapper

@use_db_session
def post_grade(session, body):
    event = gradeReport(**body)
    logger.info(f"Stored event: {event}")
    return event

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5020)
