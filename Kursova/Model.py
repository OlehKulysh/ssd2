from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Ory:33@localhost:5432/OryDB'

db = SQLAlchemy(app)


class Buildings(db.Model):
    __tablename__ = 'BUILDINGS'
    numb_building = db.Column('NUMB_BUILDING', db.String(20), primary_key=True)
    json = db.Column('JSON', db.Text)

    requests = db.relationship('Requests', backref='BUILDINGS', lazy='dynamic')

    def __init__(self, numb_building, json):
        self.numb_building = numb_building
        self.json = json

    def __repr__(self):
        return '<Faculties: numb_building=%r; json=%r>' % \
               self.numb_building, self.json


class Groups(db.Model):
    __tablename__ = 'GROUPS'
    name_group = db.Column('NAME_GROUP', db.String(20), primary_key=True)

    users = db.relationship('Users', backref='GROUPS', lazy='dynamic')
    requests = db.relationship('Requests', backref='GROUPS', lazy='dynamic')

    def __init__(self, name_group):
        self.name_group = name_group

    def __repr__(self):
        return '<Teachers: name_group=%r>' % \
               self.name_group


class Users(db.Model):
    __tablename__ = 'USERS'

    login = db.Column('LOGIN', db.String(20), primary_key=True)
    password = db.Column('PASSWORD', db.String(20))
    numb_group = db.Column('NUMB_GROUP', db.String(20), db.ForeignKey('GROUPS.NAME_GROUP'), primary_key=True)
    year = db.Column('YEAR', db.Integer, primary_key=True)

    def __init__(self, login, password, numb_group, year):
        self.login = login
        self.password = password
        self.numb_group = numb_group
        self.year = year

    def __repr__(self):
        return '<Educational Buildings: login=%r; password=%r; numb_group=%r; year=%r>' % \
               self.login, self.password, self.numb_group, self.year


class Requests(db.Model):
    __tablename__ = 'REQUESTS'

    id = db.Column('ID', db.Integer, primary_key=True)
    login = db.Column('LOGIN', db.String(20), db.ForeignKey('GROUPS.NAME_GROUP'), primary_key=True)
    building = db.Column('BUILDING', db.String(20), db.ForeignKey('BUILDINGS.NUMB_BUILDING'), primary_key=True)
    audience = db.Column('AUDIENCE', db.Integer)
    time = db.Column('TIME', db.Time)
    data = db.Column('DATA', db.Date)


    def __init__(self, id, login, building, audience, data, time):
        self.id = id
        self.login = login
        self.building = building
        self.audience = audience
        self.data = data
        self.time = time

    def __repr__(self):
        return '<Groups: id=%r; login=%r; building=%r; audience=%r; data=%r; time=%r>' % \
               self.id, self.login, self.building, self.audience, self.data, self.time

