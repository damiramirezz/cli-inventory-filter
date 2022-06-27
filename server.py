from asyncio import tasks


class Server:
    """
    Server class with id, task, environment, location and team
    """
    def __init__(self, id, task, environment, location, team):
        self._id = id
        self._task = task
        self._environment = environment
        self._location = location
        self._team = team

    # Getter
    @property
    def id(self):
        return self._id
    
    @property
    def task(self):
        return self._task

    @property
    def environment(self):
        return self._environment

    @property
    def location(self):
        return self._location

    @property
    def team(self):
        return self._team

    
    def __repr__(self):
        return f"{self._id}.{self._task}.{self._environment}.{self._location}.{self._team}\n"