from flask import jsonify
from marshmallow import ValidationError
# from flask_admin.contrib.sqla import ModelView
from src import app, jwt, api, db
from src.models import User, Comment, Subscribe, Blog

from src.resources.image import Avatar, AvatarUpload, ImageUpload, Image

from src.resources.user import UserLogout, Users, UserLogin, TokenRefresh, UserRegister
from src.resources.blog import BlogResource, BlogList
from src.resources.subscribe import SubscribeResource, SubscribeList
from src.resources.comment import CommentResource, CommentList
from src.resources.blacklist import BLACKLIST


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


# @app.before_first_request
# def create_tables():
#     db.create_all()


# @jwt.additional_claims_loader
# def add_claims_to_jwt(identity):
#     if identity == 1:
#         return {'is_admin': True}
#     return {'is_admin': False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    print(jwt_payload)
    return jsonify({"description": "Token expired", "error": "token_expired"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(jwt_payload):
    return (
        jsonify({"description": "token verification failed", "error": "invalid_token"}),
        401,
    )


@jwt.unauthorized_loader
def unauthorized_callback(error):
    return (
        jsonify(
            {
                "desctiption": "authorization failed, no access token found",
                "error": "authorization_failed",
            }
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_data):
    return (
        jsonify(
            {"description": "fresh token required", "error": "fresh_token_required"}
        ),
        401,
    )


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({"description": "token revoked", "error": "token_revoked"}), 401


@jwt.token_in_blocklist_loader
def check_blacklist(jwt_header, jwt_data):
    print(jwt_data)
    return jwt_data["jti"] in BLACKLIST


api.add_resource(BlogResource, "/add-blog")
api.add_resource(BlogList, "/blogs")
api.add_resource(SubscribeResource, "/add-subscription")
api.add_resource(SubscribeList, "/subscriptions")
api.add_resource(CommentResource, "/add-comment")
api.add_resource(CommentList, "/comments")
# api.add_resource(UserMileageResource, "/user-mileage/<int:_employee_id>")
# api.add_resource(LoginDetail, "/clockdetail/<int:_id>")
api.add_resource(UserRegister, "/register")
api.add_resource(Users, "/user/<int:_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(ImageUpload, "/upload/image")
api.add_resource(Image, "/image/<string:filename>")
api.add_resource(AvatarUpload, "/upload/avatar")
api.add_resource(Avatar, "/avatar/<int:user_id>")


# admin.add_view(ModelView(Users, db.session))
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Blog, db.session))
# admin.add_view(ModelView(Comment, db.session))
# admin.add_view(ModelView(Subscribe, db.session))


        

#dashboard
#my projects
#
# UPDATE `ass_caregiver2`
# SET    a.sdate = b.sdate
# FROM   `ass_caregiver2` a
#        INNER JOIN `ass_caregiver` b
#          ON a.employee = b.employee and a.ucode=b.ucode
# WHERE  b.employee = 35 and employee_sign is null

# SELECT * FROM `ass_caregiver2` where employee=35 AND employee_sign is null and ucode in ( SELECT ucode FROM `ass_caregiver` where employee=35 )

# SELECT * FROM `ass_caregiver` WHERE ucode=36 and employee=35

# UPDATE `ass_caregiver2` 
# SET sdate=DATE_ADD(now(), INTERVAL 1 DAY)
# where employee=35 AND employee_sign is null 
# and ucode in ( SELECT ucode FROM `ass_caregiver` where employee=35 ) 
# AND ucode=36
# and approve_date is null

