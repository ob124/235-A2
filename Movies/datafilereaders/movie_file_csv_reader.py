import csv

from Movies.domainmodel import movie
from Movies.domainmodel import actor
from Movies.domainmodel import genre
from Movies.domainmodel import director


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        if file_name == "" or type(file_name) is not str:
            self.__file_name = None
        else:
            self.__file_name = file_name.strip()
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                #print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1

                # adding to the datasets
                # build actors, genres, directors, then add to film, then add film to list
                director_name = row["Director"].strip()
                director_object = director.Director(director_name)
                if director_object in self.__dataset_of_directors:
                    pass
                else:
                    self.__dataset_of_directors.add(director_object)

                act = row["Actors"]  # ['Chris', 'Pratt,', 'Vin', 'Diesel,', 'Bradley', 'Cooper,']
                act = act.split(",")
                actor_list = []
                # need to find a way to check if each actor is in the set
                for i in range(len(act)):
                    new_act = actor.Actor(act[i])
                    actor_list.append(new_act)
                    if new_act in self.__dataset_of_actors:
                        pass
                    else:
                        self.__dataset_of_actors.add(new_act)

                gen = row["Genre"].split(",")
                genre_list = []
                # need to find a way to check if each genre is in the set
                for i in range(len(gen)):
                    new_gen = genre.Genre(gen[i])
                    genre_list.append(new_gen)
                    if new_gen in self.__dataset_of_genres:
                        pass
                    else:
                        self.__dataset_of_genres.add(new_gen)

                # build movie (also check if it exists)
                # need to add all actors, genres, and director
                new_movie = movie.Movie(title, release_year)
                new_movie.director = director_object

                for i in range(len(actor_list)):
                    new_movie.add_actor(actor_list[i])

                for i in range(len(genre_list)):
                    new_movie.add_genre(genre_list[i])

                if new_movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(new_movie)

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
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres
# test sorting of movies

