from flask import request, render_template, redirect, url_for, session, Blueprint
import Movies.adapters.repository as repo
from Movies.domainmodel.actor import Actor
from Movies.domainmodel.genre import Genre
from Movies.utilities.utilities import serialize

# use the add and get
home_blueprint = Blueprint('home_bp', __name__)
# global to keep track of search results


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    # clears any previous search upon returning to home page.
    session['search'] = None
    if session['login'] is not None:
        user_name = "Hello {0}!".format(session['login'])
    else:
        user_name = ""

    if request.method == 'POST':
        # Gets search data
        title_search = request.form['title_search']
        director_search = request.form['director_search']
        actor_search = request.form['actor_search']
        genre_search = request.form['genre_search']

        # Builds list to store in session
        ID_list = []

        # Filters using search
        if title_search != "":
            for i in range(repo.repo_instance.get_num_movies() - 1):
                if repo.repo_instance.get_movie(i).title.lower() == title_search.lower():
                    ID_list.append(i)

        if director_search != "":
            if len(ID_list) == 0:
                for i in range(repo.repo_instance.get_num_movies() - 1):
                    if repo.repo_instance.get_movie(i).director.director_full_name.lower() == director_search.lower():
                        ID_list.append(i)
            else:
                for i in range(len(ID_list)):
                    if repo.repo_instance.get_movie(i).director != director_search:
                        ID_list.pop(i)

        if actor_search != "":
            if len(ID_list) == 0:
                for i in range(repo.repo_instance.get_num_movies() - 1):
                    if Actor(actor_search) in repo.repo_instance.get_movie(i).actors:
                        ID_list.append(i)
            else:
                for i in range(len(ID_list)):
                    if Actor(actor_search) not in repo.repo_instance.get_movie(i).actors:
                        ID_list.pop(i)

        if genre_search != "":
            if len(ID_list) == 0:
                for i in range(repo.repo_instance.get_num_movies() - 1):
                    if Genre(genre_search) in repo.repo_instance.get_movie(i).genres:
                        ID_list.append(i)
            else:
                for i in range(len(ID_list)):
                    if Genre(genre_search) not in repo.repo_instance.get_movie(i).genres:
                        ID_list.pop(i)

        # Builds the url for (check if search list is empty, if it isn't then build with list in mind)
        # need a way to know if its empty from bad search or no input, bad search return to home, no input then default)
        if len(ID_list) > 0:
            search_url = url_for('movielist_bp.movielist', movieid=str(ID_list[0]))
            # save ID_list as a session var
            # need to build the ID_list as a string that can be processed.
            # this should all be done as utility.
            session_string = ""
            session_string = serialize(ID_list, session_string)
            session['search'] = session_string

        elif title_search == "" and director_search == "" and actor_search == "" and genre_search == "":
            # default search
            search_url = url_for('movielist_bp.movielist', movieid='0')
        else:
            # Search failed so the user is returned to the home page
            search_url = "/"

        return redirect(search_url)

    # should never reach here but if it does, will default to first item.
    return render_template('home/home.html', user_name=user_name)



