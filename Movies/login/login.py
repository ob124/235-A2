from flask import Blueprint
from flask import request, render_template, redirect, session
import Movies.adapters.repository as repo

login_blueprint = Blueprint('login_bp', __name__)
# global to keep track of search results


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if session['login'] is not None:
        user_name = "Hello {0}!".format(session['login'])
    else:
        user_name = None

    if request.method == 'POST':
        if request.form['button'] == "logout":
            session['login'] = None
            return redirect('/')
        else:
            username = request.form['username']
            password = request.form['password']
            # see if they match, if so login successful
            users = repo.repo_instance.get_users()
            for i in range(len(users)):
                if username == users[i].user_name and password == users[i].password:
                    session['login'] = username
                    return redirect('/')

            return redirect('/login')

    return render_template('login/login.html', user_name=user_name)
