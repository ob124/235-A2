from Movies.domainmodel.movie import Movie
from Movies.domainmodel.review import Review


class User:
    def __init__(self, user_name, password):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()

        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, other):
        if other == "" or type(other) is not str:
            self.__user_name = None
        else:
            self.__user_name = other.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        if other == "" or type(other) is not str:
            self.__password = None
        else:
            self.__password = other.strip()

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie):
        if type(movie) is Movie:
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__watched_movies.append(movie)

    def add_review(self, review):
        if type(review) is Review:
            self.__reviews.append(review)

    def __repr__(self):
        return "<User {0}>".format(self.__user_name)

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)


