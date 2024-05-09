from src import ma
from src.models import Subscribe


class SubscribeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscribe
        dump_only = ("id",)
        include_fk = True
        load_instance = True
