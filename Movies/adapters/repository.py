import abc
from Movies.domainmodel.movie import Movie


repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_movie(self, Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movieid):
        raise NotImplementedError

    @abc.abstractmethod
    def load_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_num_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def load_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username):
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_names(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, username, password):
        raise NotImplementedError

    @abc.abstractmethod
    def load_reviews(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, username, review, movie, rating):
        raise NotImplementedError

    @abc.abstractmethod
    def populate(self):
        raise NotImplementedError
