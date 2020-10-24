
class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.colleagues = set()

    @property
    def actor_full_name(self):
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, name):
        self.__actor_full_name = name

    def add_actor_colleague(self, colleague):
        self.colleagues.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.colleagues:
            return True
        else:
            return False

    def __repr__(self):
        return "<Actor {0}>".format(self.__actor_full_name)

    def __eq__(self, other):
        return other.actor_full_name.lower() == self.actor_full_name.lower()

    def __lt__(self, other):
        return self.actor_full_name.lower() < other.actor_full_name.lower()

    def __hash__(self):
        return hash(self.__actor_full_name)
