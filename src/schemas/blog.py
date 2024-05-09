from src import ma
from src.models import Blog


class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
        dump_only = ("id",)
        include_relationships = True
        include_fk = True
        load_instance = True
