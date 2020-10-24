import csv
from Movies.domainmodel.user import User


class UserFileCSVReader:
    def __init__(self, file_name: str):
        if file_name == "" or type(file_name) is not str:
            self.__file_name = None
        else:
            self.__file_name = file_name.strip()
        self.__dataset_of_users = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                username = row['username']
                password = row['password']
                self.__dataset_of_users.append(User(username, password))

    def write_csv_file(self, user_id, username, password):
        with open(self.__file_name, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([user_id, username, password])

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
    def dataset_of_users(self):
        return self.__dataset_of_users
