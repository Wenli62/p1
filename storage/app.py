import connexion
import logging
import logging.config
import yaml
import functools
from db import make_session
from models import gradeReport
import yaml
import logging, logging.config


# Load configuration files
with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open("log_conf.yml", "r") as f:
    LOG_CONFIG = yaml.safe_load(f.read())
    logging.config.dictConfig(LOG_CONFIG)

# Logger setup
logger = logging.getLogger('basicLogger')

# Set up the Connexion app
app = connexion.FlaskApp(__name__, specification_dir='')

# Add API based on the OpenAPI specification in the YAML file
app.add_api("mysql.yaml", strict_validation=True, validate_responses=True)

# Route function to handle both GET and POST requests for "/vote"

def use_db_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = make_session()
        try:
            # event_type = args[0]
            # trace_id = args[1]['trace_id']
            
            event = func(session, *args, **kwargs)
            session.add(event)
            session.commit()
        finally:
            session.close()
            # logger.debug(f"Stored event {event_type} with a trace id of {trace_id}")
    return wrapper

@use_db_session
def post_grade(session, body):
    event = gradeReport(**body)
    return event

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
