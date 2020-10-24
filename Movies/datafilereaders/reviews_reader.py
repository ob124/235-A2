import csv
import Movies.adapters.repository as repo
from Movies.domainmodel.review import Review


class ReviewFileCSVReader:
    def __init__(self, file_name: str):
        if file_name == "" or type(file_name) is not str:
            self.__file_name = None
        else:
            self.__file_name = file_name.strip()
        self.__dataset_of_reviews = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                username = row['username']
                movie_id = int(row['movie_id'])
                review = row['review']
                rating = int(row['rating'])
                # grabs movie
                movie = repo.repo_instance.get_movie(movie_id)
                # builds review and adds it to list
                user_review = Review(movie, review, rating)
                self.__dataset_of_reviews.append(user_review)
                # grabs user and adds review to it
                user = repo.repo_instance.get_user(username)
                user.add_review(user_review)
                user_review.user = user

    def write_csv_file(self, review_id, username, movie, review, rating):
        with open(self.__file_name, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([review_id, username, movie, review, rating])

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, other):
        if other == "" or type(other) is not str:
            self.__file_name = None
        else:
            self.__file_name = other.strip()

    @property
    def dataset_of_reviews(self):
        return self.__dataset_of_reviews
