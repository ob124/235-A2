
class Genre:
    def __init__(self, name):
        if name == "" or type(name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = name.strip()

    @property
    def genre_name(self):
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name):
        self.__genre_name = genre_name

    def __repr__(self):
        return "<Genre {0}>".format(self.__genre_name)

    def __eq__(self, other):
        return other.genre_name.lower() == self.genre_name.lower()

    def __lt__(self, other):
        return self.genre_name.lower() < other.genre_name.lower()

    def __hash__(self):
        return hash(self.__genre_name)
