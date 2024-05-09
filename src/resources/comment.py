from datetime import datetime, timedelta
import json
from flask import request
from flask_jwt_extended import (
    jwt_required,
)
from flask_restful import Resource
from src.models import Comment
from src.resources.blacklist import BLACKLIST
from src.schemas.comment import CommentSchema

comment_schema = CommentSchema()
comment_list_schema = CommentSchema(many=True)


class CommentResource(Resource):
    @classmethod
    def post(cls):
        comment = comment_schema.load(request.get_json())

        comment.save_to_db()

        return comment_schema.dump(comment), 201

    

    @classmethod
    @jwt_required()
    def delete(cls, _id: int):
        comment = Comment.find_by_id(_id)
        if not comment:
            return {"message": "assessment not found"}, 404
        comment.delete_from_db()
        return {"message": "assessment deleted."}, 200

    @classmethod
    def put(cls, _id: int):
        comment_json = request.get_json()

        comment = Comment.find_by_id(_id)

        if comment:
            comment = comment_schema.load(comment_json)

        comment.save_to_db()

        return comment_schema.dump(comment), 200

class CommentList(Resource):
    @classmethod
    #@jwt_required()
    def get(cls):
        return {"comment": comment_list_schema.dump(Comment.find_all())}, 200