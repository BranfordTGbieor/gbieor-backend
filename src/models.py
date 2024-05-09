from typing import List
from datetime import datetime, date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from src import db

day = date.today() #+ timedelta(days=1)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, index=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    username = db.Column(db.String(30))
    password = db.Column(db.String(150))
    usertype = db.Column(db.String(100))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(100))
    photo = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

      # hash user password input
    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    # verify user password input hash with existing password hash
    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "User":
        return cls.query.filter_by(id=_id).first()

class Blog(db.Model):

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    blog_title = db.Column(db.String(200))
    headline_image = db.Column(db.String(100))
    blog_body = db.Column(db.String(500))
    blog_image_one = db.Column(db.String(100))
    blog_image_two = db.Column(db.String(100))
    blog_image_three = db.Column(db.String(100))
    blog_image_four = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id: int) -> "Blog":
        return cls.query.filter_by(id=_id).first()


    @classmethod
    def find_all(cls) -> List["Blog"]:
        return cls.query.all()
    

class Comment(db.Model):

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    blog_id = db.Column(db.BigInteger, db.ForeignKey('blog.id'))
    user_comment = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id: int) -> "Blog":
        return cls.query.filter_by(id=_id).first()


    @classmethod
    def find_all(cls) -> List["Blog"]:
        return cls.query.all()
    

class Subscribe(db.Model):

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    subscribed = db.Column(db.Boolean, default=False, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id: int) -> "Blog":
        return cls.query.filter_by(id=_id).first()


    @classmethod
    def find_all(cls) -> List["Blog"]:
        return cls.query.all()


     


