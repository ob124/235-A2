class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self):
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, name):
        self.__director_full_name = name

    def __repr__(self):
        return "<Director {0}>".format(self.__director_full_name)

    def __eq__(self, other):
        return other.director_full_name.lower() == self.director_full_name.lower()

    def __lt__(self, other):
        return self.director_full_name.lower() < other.director_full_name.lower()

    def __hash__(self):
        return hash(self.__director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None
