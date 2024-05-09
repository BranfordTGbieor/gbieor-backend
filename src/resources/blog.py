from datetime import datetime, timedelta
import json
from flask import request
from flask_jwt_extended import (
    jwt_required,
)
from flask_restful import Resource
from src.models import Blog
from src.resources.blacklist import BLACKLIST
from src.schemas.blog import BlogSchema

blog_schema = BlogSchema()
blog_list_schema = BlogSchema(many=True)


class BlogResource(Resource):
    @classmethod
    def post(cls):
        blog = blog_schema.load(request.get_json())

        blog.save_to_db()

        return blog_schema.dump(blog), 201

    

    @classmethod
    @jwt_required()
    def delete(cls, _id: int):
        blog = Blog.find_by_id(_id)
        if not blog:
            return {"message": "assessment not found"}, 404
        blog.delete_from_db()
        return {"message": "assessment deleted."}, 200

    @classmethod
    def put(cls, _id: int):
        blog_json = request.get_json()

        blog = Blog.find_by_id(_id)

        if blog:
            blog = blog_schema.load(blog_json)

        blog.save_to_db()

        return blog_schema.dump(blog), 200

class BlogList(Resource):
    @classmethod
    #@jwt_required()
    def get(cls):
        return {"blog": blog_list_schema.dump(Blog.find_all())}, 200