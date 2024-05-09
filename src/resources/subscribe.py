from datetime import datetime, timedelta
import json
from flask import request
from flask_jwt_extended import (
    jwt_required,
)
from flask_restful import Resource
from src.models import Subscribe
from src.resources.blacklist import BLACKLIST
from src.schemas.subscribe import SubscribeSchema

subscribe_schema = SubscribeSchema()
subscribe_list_schema = SubscribeSchema(many=True)


class SubscribeResource(Resource):
    @classmethod
    def post(cls):
        subscribe = subscribe_schema.load(request.get_json())

        subscribe.save_to_db()

        return subscribe_schema.dump(subscribe), 201

    

    @classmethod
    @jwt_required()
    def delete(cls, _id: int):
        subscribe = Subscribe.find_by_id(_id)
        if not subscribe:
            return {"message": "subscription not found"}, 404
        subscribe.delete_from_db()
        return {"message": "subscription deleted."}, 200

    @classmethod
    def put(cls, _id: int):
        subscribe_json = request.get_json()

        subscribe = Subscribe.find_by_id(_id)

        if subscribe:
            subscribe = subscribe_schema.load(subscribe_json)

        subscribe.save_to_db()

        return subscribe_schema.dump(subscribe), 200

class SubscribeList(Resource):
    @classmethod
    #@jwt_required()
    def get(cls):
        return {"subscribe": subscribe_list_schema.dump(Subscribe.find_all())}, 200