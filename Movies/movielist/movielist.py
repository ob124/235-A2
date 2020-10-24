from flask import Blueprint
from flask import render_template, request, redirect, url_for, session
import Movies.adapters.repository as repo

# use the add and get
movielist_blueprint = Blueprint('movielist_bp', __name__)


@movielist_blueprint.route('/movie/<movieid>', methods=['GET', 'POST'])
def movielist(movieid):
    next_movie = ""
    previous_movie = ""
    movie_id = int(movieid)
    movie = repo.repo_instance.get_movie(movie_id)

    if session['login'] is not None:
        user_name = "Hello {0}!".format(session['login'])
    else:
        user_name = None

    if request.method == 'POST':
        # Grab user
        user = session['login']
        # submit review
        repo.repo_instance.add_review(user, movie_id, request.form['new_review'], int(request.form['rating']))
        return redirect(url_for('movielist_bp.movielist', movieid=str(movie_id)))

    if session['search'] is not None:
        session_string = session['search'].split()
        id_location = session_string.index(movieid)

        if id_location + 1 < len(session_string):
            next_movie = url_for('movielist_bp.movielist', movieid=session_string[id_location + 1])
        else:
            next_movie = url_for('movielist_bp.movielist', movieid=session_string[id_location])

        if id_location - 1 > 0:
            previous_movie = url_for('movielist_bp.movielist', movieid=session_string[id_location - 1])
        else:
            previous_movie = url_for('movielist_bp.movielist', movieid=session_string[id_location])
    else:
        # check that the next_list doesn't out of bounds
        if movie_id + 1 <= repo.repo_instance.get_num_movies() - 1:
            next_movie = url_for('movielist_bp.movielist', movieid=str(movie_id + 1))
        else:
            next_movie = url_for('movielist_bp.movielist', movieid=str(movie_id))

        if movie_id-1 >= 0:
            previous_movie = url_for('movielist_bp.movielist', movieid=str(movie_id - 1))
        else:
            previous_movie = url_for('movielist_bp.movielist', movieid=str(movie_id))

    # Sets up the movie names based off the page_num
    movie_title = movie.title

    # grabs director, actors, and genres and converts them to string format
    movie_directors = "Director: {0}.".format(movie.director.director_full_name)

    movie_actors = "Actors: "
    for i in range(len(movie.actors)):
        movie_actors += movie.actors[i].actor_full_name
        if i < len(movie.actors) - 1:
            movie_actors += ", "
        else:
            movie_actors += "."

    movie_genres = "Genres: "
    for i in range(len(movie.genres)):
        movie_genres += movie.genres[i].genre_name
        if i < len(movie.genres) - 1:
            movie_genres += ", "
        else:
            movie_genres += "."

    # builds the movie text string for the page
    movie_description = [movie_directors, "\n", movie_actors, "\n", movie_genres]

    # grab reviews then puts all relevant ones into a new list.
    reviews = repo.repo_instance.get_reviews()
    movie_reviews = list()
    for i in range(len(reviews)):
        if reviews[i].movie == movie:
            movie_reviews.append(reviews[i])

    # grabs the text from each relevant review
    final_review_list = list()
    for i in range(len(movie_reviews)):
        final_review_list.append("User: {0}".format(movie_reviews[i].user.user_name))
        final_review_list.append("Rating:{0}".format(movie_reviews[i].rating))
        final_review_list.append(movie_reviews[i].review_text)
        final_review_list.append("----------")
    # need to grab the user

    return render_template('movielist/movielist.html', next_list=next_movie, previous_list=previous_movie,
                           movie_description=movie_description, movie_title=movie_title, user_name=user_name,
                           movie_reviews=final_review_list, movie_id=movie_id)
