from datetime import datetime, timedelta
import json
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Resource
from src.models import User
from src.resources.blacklist import BLACKLIST
from src.schemas.user import UserSchema

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user = user_schema.load(request.get_json())

        if user.find_by_username(user.username):
            return {"message": "A user with that username already exists"}, 400

        if user.find_by_email(user.email):
            return {"message": "A user with that email already exists"}, 400

        user.set_password(user.password)

        user.save_to_db()

        return {"message": "User created successfully."}, 201


class Users(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """

    @classmethod
    def put(cls, _id: int):
        user_json = user_schema.load(request.get_json())

        user = user_json.find_by_id(_id)
        # print(client)
        
        # print(caregiver_json["worker_signature"])
        if user:
            user.employee = user_json["employee"]
            user.save_to_db()
        else:
            return {"message": "client not found"}, 404

        return user_schema.dump(user), 200


    # @classmethod
    # def put(cls, _id: int):
    #     user_json = request.get_json()

    #     user = User.find_by_id(_id)

    #     if user:
    #         user.set_password(user.password)
    #         user = user_schema.load(user_json)

    #     user.save_to_db()

    #     return user_schema.dump(user), 200

    @classmethod
    def get(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {"message": "User Not Found"}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {"message": "User Not Found"}, 404
        user.delete_from_db()
        return {"message": "User deleted."}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data = user_schema.load(request.get_json())

        user = user_data.find_by_email(user_data.email)
        expires = datetime.now() + timedelta(hours=24)

        if user and user.check_password(user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, 
            "refresh_token": refresh_token,
            "email":user.email,
            "firstname": user.firstname,
            "lastname": user.firstname,
            "phone": user.phone,
            "usertype": user.usertype,
            "user_id": user.id,
            "token_expires": datetime.strptime(str(expires), "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S.%f")
            }, 200
        return {"message": "invalid credentials"}, 401


class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()["jti"]  # jti is jwt id
        print(jti)
        BLACKLIST.add(jti)
        return {"message": "logged out successfully"}


class TokenRefresh(Resource):
    @classmethod
    @jwt_required(refresh=True)
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
