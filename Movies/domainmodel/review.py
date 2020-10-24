from Movies.domainmodel.movie import Movie


class Review:
    def __init__(self, start_movie, start_review, start_rating):
        self.__movie = start_movie
        if start_review == "" or type(start_review) is not str:
            self.__review_text = None
        else:
            self.__review_text = start_review.strip()
        if 0 < start_rating <= 10 and type(start_rating) is int:
            self.__rating = start_rating
        else:
            self.__rating = None
        self.__timestamp = None
        self.__user = None

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
            self.__user = user

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        self.__movie = new_movie

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, new_review):
        if new_review == "" or type(new_review) is not str:
            self.__review_text = None
        else:
            self.__review_text = new_review.strip()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if 0 < new_rating <= 10 and type(new_rating) is int:
            self.__rating = new_rating
        else:
            self.__rating = None

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, name):
        if name > 0 and type(name) is int:
            self.__timestamp = name

    def __repr__(self):
        return "<Review {0}, {1}>".format(self.__movie, self.__timestamp)

    def __eq__(self, other):
        return (self.movie, self.review_text, self.rating, self.timestamp) == (other.movie, other.review_text, other.rating, other.timestamp)
