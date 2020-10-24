
from Movies.adapters.repository import AbstractRepository, RepositoryException
import Movies.datafilereaders.movie_file_csv_reader as importer
from Movies.datafilereaders.reviews_reader import ReviewFileCSVReader
from Movies.datafilereaders.users_reader import UserFileCSVReader
from Movies.domainmodel.user import User
from Movies.domainmodel.review import Review


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._movies = list()
        self._genres = list()
        self._actors = list()
        self._directors = list()
        self._users = list()
        self._reviews = list()

    def load_movies(self):
        filename = 'Movies/datafiles/Data1000Movies.csv'
        movie_file_reader = importer.MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        self._movies = movie_file_reader.dataset_of_movies
        self._genres = movie_file_reader.dataset_of_genres
        self._actors = movie_file_reader.dataset_of_actors
        self._directors = movie_file_reader.dataset_of_directors

    def get_movie(self, movieid):
        if 0 <= movieid < len(self._movies):
            return self._movies[movieid]
        else:
            return

    def get_num_movies(self):
        return len(self._movies)

    def load_users(self):
        file_name = 'Movies/datafiles/users.csv'
        user_reader = UserFileCSVReader(file_name)
        user_reader.read_csv_file()
        self._users = user_reader.dataset_of_users

    def get_user(self, username):
        for i in range(len(self._users)):
            if self._users[i].user_name == username:
                return self._users[i]

    def get_users(self):
        return self._users

    def get_user_names(self):
        names = list()
        for i in range(len(self._users)):
            names.append(self._users[i].user_name)
        return names

    def add_user(self, username, password):
        file_name = 'Movies/datafiles/users.csv'
        user_reader = UserFileCSVReader(file_name)
        user_reader.write_csv_file(len(self._users), username, password)
        self._users.append(User(username, password))

    def load_reviews(self):
        file_name = 'Movies/datafiles/reviews.csv'
        review_reader = ReviewFileCSVReader(file_name)
        review_reader.read_csv_file()
        self._reviews = review_reader.dataset_of_reviews

    def get_reviews(self):
        return self._reviews

    def add_review(self, username, movie_id, review, rating):
        file_name = 'Movies/datafiles/reviews.csv'
        review_reader = ReviewFileCSVReader(file_name)
        review_reader.write_csv_file(len(self._reviews), username, movie_id, review, rating)
        # need to convert movie_id to actual movie here
        user_review = Review(self.get_movie(movie_id), review, rating)
        self._reviews.append(user_review)
        # user name is unique so search by that when adding a review to a user
        user = ""
        for i in range(len(self._users)):
            if self._users[i].user_name == username:
                user = self._users[i]
        user.add_review(user_review)
        user_review.user = user

    def populate(self):
        self.load_movies()
        self.load_users()
        self.load_reviews()
