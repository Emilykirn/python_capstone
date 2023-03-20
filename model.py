
import os
from flask_sqlalchemy import SQLAlchemy  
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(99), unique = True, nullable = False)
    password = db.Column(db.String(99), nullable = False)

    rosters = db.relationship("Roster", backref="user")
    trainings = db.relationship("Training", backref="user")
    
    def __repr__(self):
        return f'User user_id={self.id} email={self.email}'
        
class Roster(db.Model):

    __tablename__= "rosters"

    roster_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    coach_name = db.Column(db.String)
    team_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    players = db.relationship("Player", backref="roster")

    def __repr__(self):
        return f'Roster roster_id={self.roster_id}, coach={self.coach}, team_name={self.team_name}'

class Player(db.Model):

    __tablename__= "players"

    player_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    player_number = db.Column(db.Integer, unique = True)
    player_position = db.Column(db.String)
    roster_id = db.Column(db.Integer, db.ForeignKey("rosters.roster_id"))
    
    def __repr__(self):
        return f'Player player_id={self.player_id}, first_name={self.first_name}, last_name={self.last_name}'


class Training(db.Model):
    __tablename__ = "trainings"

    training_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    link = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __repr__(self):
        return f'Training training_id={self.training_id}, link={self.link}'
    

def connect_to_db(flask_app, db_uri="postgresql:///ballers", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the cool DATABASE!")


if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)