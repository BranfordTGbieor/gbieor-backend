from src import ma
from src.models import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        dump_only = ("id",)
        include_fk = True
        load_instance = True
