from src import ma
from src.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True
