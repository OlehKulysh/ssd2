from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, TextField, TimeField, DateField
from wtforms import validators



class RequestsUserForm(Form):

    id = IntegerField("ID: ", [validators.data_required("Please, enter year of enrollment.")])
    login = StringField("Login: ", [validators.data_required("Please, enter login.")])
    building = StringField("Building: ", [validators.data_required("Please, enter login.")])
    audience = IntegerField("Audience: ", [validators.data_required("Please, enter year of enrollment.")])
    time = TimeField("Time: ", [validators.data_required("Please, enter year of enrollment.")])
    data = DateField("Date: ", [validators.data_required("Please, enter year of enrollment.")])

    submit = SubmitField("Enter")


class RequestsForm(Form):

    building = StringField("Building: ", [validators.data_required("Please, enter login.")])
    audience = IntegerField("Audience: ", [validators.data_required("Please, enter year of enrollment.")])

    submit = SubmitField("Enter")


class SingInForm(Form):

    login = StringField("Login: ", [validators.data_required("Please, enter login.")])
    password = StringField("Password: ", [validators.data_required("Please, enter password.")])

    submit = SubmitField("Enter")


class BuildingsForm(Form):

    numb_building = StringField("Number: ", [validators.data_required("Please, enter the case number: ")])
    json = TextField("Path: ", [validators.data_required("Please, enter PATH map of the case: ")])

    submit = SubmitField("Enter")


class GroupsForm(Form):

    name_group = StringField("Name: ", [validators.data_required("Please, enter group name: ")])

    submit = SubmitField("Enter")


class UsersForm(Form):

    login = StringField("Login: ", [validators.data_required("Please, enter login.")])
    password = StringField("Password: ", [validators.data_required("Please, enter password.")])
    numb_group = StringField("Number: ", [validators.data_required("Please, enter group number.")])
    year = IntegerField("Year: ", [validators.data_required("Please, enter year of enrollment.")])

    submit = SubmitField("Enter")
