import os

baseddir = os.path.abspath(os.path.dirname(__file__))
# define app configurations here
class Config(object):
    # flas app secret
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "send-me-a-message"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(baseddir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "amazing-a-message"
    UPLOADED_IMAGES_DEST = os.path.join("static", "images")
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
