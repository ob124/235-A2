from Movies.domainmodel.director import Director


class Movie:
    def __init__(self, title: str, release: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if type(release) is not int and release < 1900:
            self.__release = None
        else:
            self.__release = release
        self.__description = ""
        self.__director = None
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = 0

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, name):
        if name == "" or type(name) is not str:
            self.__title = None
        else:
            self.__title = name.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if type(new_description) is str:
            self.__description = new_description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, new_director):  # check it is a director
        if type(new_director) is Director:
            self.__director = new_director

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if runtime > 0:
            self.__runtime_minutes = runtime
        else:
            raise ValueError

    @property
    def release(self):
        return self.__release

    @release.setter
    def release(self, date):
        if type(date) is not int and date < 1900:
            pass
        else:
            self.__release = date

    def add_actor(self, actor_add):
        self.__actors.append(actor_add)

    def add_genre(self, genre):
        self.__genres.append(genre)

    def remove_actor(self, actor_remove):
        if actor_remove in self.__actors:
            self.__actors.remove(actor_remove)
        else:
            pass

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
        else:
            pass

    def __repr__(self):
        return "<Movie {0}, {1}>".format(self.__title, self.__release)

    def __eq__(self, other):
        return (other.title.lower(), other.__release) == (self.title.lower(), self.__release)

    def __lt__(self, other):
        return (self.title.lower(), self.__release) < (other.title.lower(), other.__release)

    def __hash__(self):
        return hash(self.__title + str(self.__release))