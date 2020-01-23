import plotly
import plotly.graph_objs as go
import json
from datetime import datetime

from flask import render_template, flash, request, redirect, session
from Model import *
from WTForms import *

app.secret_key = 'development key'


def setOldUser(login):
    us = open('oldUser', 'w')
    us.write(login)
    us.close()


def OldUser():
    us = open('oldUser', 'r')
    nam = us.read()
    us.close()
    return nam

def setCurrentUser(login):
    us = open('user.txt', 'w')
    us.write(login)
    us.close()


def CurrentUser():
    us = open('user.txt', 'r')
    nam = us.read()
    us.close()
    return nam


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', userName=CurrentUser())


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = RequestsForm()

    if request.method == 'POST':
        if not form.validate() or (len(form.building.data) > 20) \
                or (form.audience.data < 100) \
                or (form.audience.data > 121):
            flash('All fields are required')
            return render_template('search.html', form=form, error="Не коректно введені дані", admin=CurrentUser())
        else:
            user = Buildings.query.filter_by(numb_building=form.building.data).first()
            if user is not None:
                now = datetime.now()
                requestq = Requests(
                    id=cheakID(len(Requests.query.filter_by().all())),
                    login=CurrentUser(),
                    building=form.building.data,
                    audience=form.audience.data,
                    data='{}-{}-{}'.format(now.year, now.month, now.day),
                    time='{}:{}:{}'.format(now.hour, now.minute, now.second)
                )
                db.session.add(requestq)
                db.session.commit()
                mapForm = Buildings.query.filter_by(numb_building=form.building.data).first()
                return render_template('map.html', form=mapForm, admin=CurrentUser())
            return render_template('search.html', form=form, error="Даного корпусу не існує", admin=CurrentUser())
    return render_template("search.html", form=form, admin=CurrentUser())


def cheakID(countID):
    if Requests.query.filter_by(id=countID).first() is None:
        return countID
    else:
        return cheakID(countID + 1)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = UsersForm()
    return render_template('sign_up.html', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SingInForm()
    if request.method == 'POST':
        if not form.validate() or (len(form.login.data) > 20) or (len(form.password.data) > 20):
            flash('All fields are required')
            return render_template('sign_in.html', form=form, error="Не коректно введені дані")
        else:
            user = Users.query.filter_by(login=form.login.data).first()
            if user is not None:
                if user.password.replace(' ', '') != form.password.data:

                    return render_template('sign_in.html', form=form, error="Неправильний логін або пароль")
                else:
                    setCurrentUser(form.login.data)
                    form = RequestsForm()

                    return render_template('search.html', form=form, admin=CurrentUser())

    return render_template("sign_in.html", form=form)


@app.route('/edit_building', methods=['GET', 'POST'])
def edit_building():
    form = BuildingsForm()
    select_result = Buildings.query.filter_by().all()

    if request.method == 'POST':

        if not form.validate():
            flash('All fields are required')
            return render_template('edit_buildings.html', data=select_result, form=form)
        else:
            building = Buildings.query.filter_by(numb_building=form.numb_building.data).first()
            building.numb_building = form.numb_building.data
            building.json = form.json.data
            db.session.commit()
            return render_template("buildings.html", data=select_result, form=form)

    return render_template("buildings.html", data=select_result, form=form)


@app.route('/buildings', methods=['GET', 'POST'])
def buildings():
    form = BuildingsForm()
    select_result = Buildings.query.filter_by().all()

    if request.method == 'POST':

        selected_build = request.form.get('del')
        if selected_build is not None:
            delOllBulidInRequest(selected_build)
            selected_row = Buildings.query.filter_by(numb_building=selected_build).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('buildings.html', data=select_result, form=form)

        selected_build = request.form.get('edit')
        if selected_build is not None:
            selected_row = Buildings.query.filter_by(numb_building=selected_build).first()
            session['building_edit_pk_data'] = selected_build
            return render_template("edit_building.html", row=selected_row, form=form, error="Не коректновведені дані")

        if not form.validate() or (len(form.numb_building.data) > 20):
            flash('All fields are required.')
            return render_template('buildings.html', data=select_result, form=form, error="Дані введені не коректно")
        else:
            if Buildings.query.filter_by(numb_building=form.numb_building.data).first() is None:
                building = Buildings(numb_building=form.numb_building.data,
                                     json=form.json.data)
                db.session.add(building)
                db.session.commit()
                select_result.append(building)
            else:
                return render_template('buildings.html', data=select_result, form=form, error="Дана будівля вже існує")

    return render_template('buildings.html', data=select_result, form=form)

def delOllBulidInRequest(numb):
    if Requests.query.filter_by(building=numb).first() is None:
        return True
    else:
        selected_row = Requests.query.filter_by(building=numb).first()
        db.session.delete(selected_row)
        db.session.commit()
        return delOllBulidInRequest(numb)


# @app.route('/edit_group', methods=['GET', 'POST'])
# def edit_group():
#     form = GroupsForm()
#     select_result = Groups.query.filter_by().all()
#
#     if request.method == 'POST':
#         if not form.validate() \
#                 or (len(form.password.data) > 20) \
#                 or (len(form.numb_group.data) > 20) \
#                 or (datetime.now().year - 4 > form.year.data) \
#                 or (form.year.data > datetime.now().year):
#             flash('All fields are required.')
#             return render_template('edit_group.html', error="Дані введені не коректно")
#         else:
#             group = Groups.query.filter_by(name_group=кщ).first()
#             group.name_group = form.name_group.data
#             return render_template("groups.html", data=select_result, form=form)
#
#     return render_template("groups.html", data=select_result, form=form)


@app.route('/groups', methods=['GET', 'POST'])
def groups():
    form = GroupsForm()
    select_result = Groups.query.filter_by().all()

    if request.method == 'POST':

        selected_number = request.form.get('del')
        if selected_number is not None:
            delOllGroupInUser(selected_number)
            selected_row = Groups.query.filter_by(name_group=selected_number).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('groups.html', data=select_result, form=form)

        selected_number = request.form.get('edit')
        if selected_number is not None:
            selected_row = Groups.query.filter_by(name_group=selected_number).first()
            session['group_edit_pk_data'] = selected_number
            return render_template("edit_group.html", row=selected_row, form=form)

        if not form.validate() or (len(form.name_group.data) > 20):
            flash('All fields are required.')
            return render_template('groups.html', data=select_result, form=form, error="Не коректновведені дані")
        else:
            if Groups.query.filter_by(name_group=form.name_group.data).first() is None:
                group = Groups(form.name_group.data)
                db.session.add(group)
                db.session.commit()
                select_result.append(group)
            else:
                render_template('groups.html', data=select_result, form=form, error="Дана група вже існує")

    return render_template('groups.html', data=select_result, form=form)

def delOllGroupInUser(group):
    if Users.query.filter_by(numb_group=group).first() is None:
        return True
    else:
        selected_row = Users.query.filter_by(numb_group=group).first()
        db.session.delete(selected_row)
        db.session.commit()
        return delOllGroupInUser(group)


@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    form = UsersForm()
    select_result = Users.query.filter_by().all()
    row = Users.query.filter_by(login=form.login.data).first()
    if request.method == 'POST':
        if form.validate() \
                or (len(form.login.data) > 20) \
                or (len(form.password.data) > 20) \
                or (len(form.numb_group.data) > 20) \
                or (datetime.now().year - 4 > form.year.data) \
                or (form.year.data > datetime.now().year):
            flash('All fields are required')

            return render_template('edit_user.html', data=select_result, row=row, form=form, error="Не коректно введені дані")
        else:
            if Groups.query.filter_by(name_group=form.numb_group.data).first() is not None:
                user = Users.query.filter_by(login=OldUser()).first()
                user.password = form.password.data
                user.numb_group = form.numb_group.data
                user.year = form.year.data
                db.session.commit()
            else:
                render_template('edit_user.html', data=select_result, row=row, form=form,
                                error="Групи не існує")


            return render_template("users.html", data=select_result, form=form)

    return render_template("users.html", data=select_result, form=form, error="Не коректновведені дані")


@app.route('/users', methods=['GET', 'POST'])
def users():
    form = UsersForm()
    select_result = Users.query.filter_by().all()

    if request.method == 'POST':

        selected_name = request.form.get('del')
        if selected_name is not None:
            selected_row = Users.query.filter_by(login=selected_name).first()
            delOllUserInRequest(selected_name)
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('users.html', data=select_result, form=form)

        selected_name = request.form.get('edit')
        if selected_name is not None:

            selected_row = Users.query.filter_by(login=selected_name).first()
            setOldUser(selected_row.login)
            return render_template("edit_user.html", row=selected_row, form=form)

        if form.validate_on_submit() \
                or (len(form.login.data) > 20) \
                or (len(form.password.data) > 20) \
                or (len(form.numb_group.data) > 20) \
                or (datetime.now().year - 4 > form.year.data) \
                or (form.year.data > datetime.now().year):

            flash('All fields are required.')
            # print(form.login.validate_on_submit())
            return render_template('sign_up.html', data=select_result, form=form, error="Не коректно введені дані")
        else:
            if Users.query.filter_by(login=form.login.data).first() is None:
                if Groups.query.filter_by(name_group=form.numb_group.data).first() is not None:
                    user = Users(
                        form.login.data,
                        form.password.data,
                        form.numb_group.data,
                        form.year.data
                    )
                    db.session.add(user)
                    db.session.commit()
                    select_result.append(user)
                    setCurrentUser(form.login.data)
                else:
                    return render_template('sign_up.html', form=form, error="Номер групи введений "
                                                                            "не коректно")

                return render_template('search.html', form=RequestsForm())
            else:
                return render_template('sign_up.html', data=select_result, form=form,
                                       error="Даний користувач вже існує")

    return render_template('users.html', data=select_result, form=form)

def delOllUserInRequest(login):
    if Requests.query.filter_by(login=login).first() is None:
        return True
    else:
        selected_row = Requests.query.filter_by(login=login).first()
        db.session.delete(selected_row)
        db.session.commit()
        return delOllUserInRequest(login)


@app.route('/requests', methods=['GET', 'POST'])
def user():
    form = RequestsUserForm()
    userData = Users.query.filter_by(login=CurrentUser())
    if CurrentUser() == "admin":
        select_result = Requests.query.filter_by().all()
    else:
        select_result = Requests.query.filter_by(login=CurrentUser()).all()

    if request.method == 'POST':
        selected_name = request.form.get('del')
        if selected_name is not None:
            selected_row = Requests.query.filter_by(id=selected_name).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)

            return render_template('requests.html',  userData=userData, data=select_result, form=form, admin=CurrentUser())

        selected_name = request.form.get('del_oll')
        if selected_name is not None:
            delOll(CurrentUser(), select_result)

            return render_template('requests.html', userData=userData, data=select_result, form=form, admin=CurrentUser())


    # print(userData[0].login, userData.password, userData.numb_group)
    return render_template('requests.html', userData=userData, data=select_result, form=form, admin=CurrentUser())

def delOll(login, select_result):
    if Requests.query.filter_by(login=CurrentUser()).first() is None:
        return []
    else:
        selected_row = Requests.query.filter_by(id=login).first();
        db.session.delete(selected_row)
        db.session.commit()
        select_result.remove(selected_row)
        return delOll(login, select_result)

if __name__ == '__main__':
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(debug=True)
