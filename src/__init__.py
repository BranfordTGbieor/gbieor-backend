from flask import Flask
# from flask_admin import Admin
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_uploads import configure_uploads
from src.libs.image_helper import IMAGE_SET
from config import Config
from flask_restful_swagger import swagger


app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')
app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrage = Migrate(app, db)
ma = Marshmallow(app)
# admin = Admin(app, name='EWCC', template_mode='bootstrap3')
CORS(app)
configure_uploads(app, IMAGE_SET)

# WSGI Web Server Gateway Interface

if __name__ == '__main__':
    app.run()

from src import routes, resources, models
