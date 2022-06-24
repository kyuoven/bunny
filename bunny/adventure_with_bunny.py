class Path(object):
    def __init__(self, name, location, monster):
        self.name = name
        self.location = location
        self.monster = monster


starting_path = Path(
    "An open field filled with flora",
    "Located in the center",
    "There are no monsters here",
)
