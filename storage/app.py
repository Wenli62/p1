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


SECRET_KEY = "3495project1"

def validate_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  # Adjust algorithm as needed
        return decoded  # Return user data from the token
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

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

# @app.route('/submit_grade', methods=['POST'])
# def submit_grade():
#     # Retrieve token from headers
#     logger.info(f"Received headers: {connexion.request.headers}")
#     auth_header = connexion.request.headers.get('Authorization')
#     if not auth_header or not auth_header.startswith("Bearer "):
#         return {"error": "Unauthorized, missing token"}, 401

#     token = auth_header.split(" ")[1]  # Extract token

#     # Validate token
#     user_data = validate_token(token)
#     if not user_data:
#         logger.warning(f"Token validation failed for token: {token}")
#         return {"error": "Unauthorized, invalid token"}, 401

#     # If token is valid, proceed to handle grade data
#     body = connexion.request.get_json()
#     event = post_grade(body)
#     return {"message": "Grade submitted successfully", "gradeReport": event}, 201


@use_db_session
def post_grade(session, body):
    event = gradeReport(**body)
    logger.info(f"Stored event: {event}")
    return event

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5020)
