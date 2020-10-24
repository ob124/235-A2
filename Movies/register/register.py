from flask import Blueprint, flash
from flask import request, render_template, redirect, session, url_for
import Movies.adapters.repository as repo

register_blueprint = Blueprint('register_bp', __name__)
# global to keep track of search results


@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # see if credentials are valid and that the user doesn't already exist
        if len(username) >= 3 and len(password) >= 6 and username not in repo.repo_instance.get_user_names():
            session['login'] = username
            repo.repo_instance.add_user(username, password)
            return redirect('/')
        else:
            if username in repo.repo_instance.get_user_names():
                return redirect(url_for("register_bp.register"))
            if len(password) < 6:
                return redirect(url_for("register_bp.register"))
            else:
                return redirect(url_for("register_bp.register"))

    return render_template('login/register.html')
