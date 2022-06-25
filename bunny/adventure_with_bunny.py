# the main adventure


class Path(object):
    def __init__(self, description, location, monsters):
        self.description = description
        self.location = location
        self.monsters = monsters
        self.paths = {}

    def go(self, direction):
        default = self.paths.get("*")
        return self.paths.get(direction, default)

    def add_paths(self, paths):
        self.paths.update(paths)


def load_room(name):
    # This line defines the function 'load_room' which has one parameter.
    return globals().get(name)
    # This line returns the value of the key name if it is found in globals (dict)


def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key


def test():
    return globals()


starting_path = Path(  # starting path, center
    "An open field filled with flora.",
    "Located in the center.",
    "There are no monsters here",
)

north_one = Path(  # What is possible here: You can rest here, or forrage for mushrooms/crops (carrots for bunny)
    "A collection of spruce trees.",
    "A path North of the field.",
    "Monsters placeholder",
)
north_two = (
    Path(  # What is possible here: get pot and flowers to make flower crown for bunny
        "An old camp lays abandoned here.",
        "A path North of the spruce trees.",
        "Monsters placeholder",
    )
)

north_east = Path(  # What is possible here: get matches
    "Name placeholder",
    "A path North-East of the field.",
    "Monsters placeholder",
)

east_one = Path(  # What is possible here: go inside machine , get lighter fluid
    "A little open area with a machine that's almost fully overtaken by nature.",
    "A path East of the field.",
    "Monsters placeholder",
)
east_two = Path(  # What is possible here:
    "Name placeholder",
    "A path East of the weird machine.",
    "Monsters placeholder",
)

south_east = Path(  # What is possible here:
    "Name placeholder",
    "A path South-East of the field.",
    "Monsters placeholder",
)

south_one = Path(  # What is possible here:
    "There's a nice pond here.",
    "A path South of the field.",
    "Monsters placeholder",
)
south_two = Path(  # What is possible here:
    "Name placeholder",
    "A path South of the pond",
    "Monsters placeholder",
)

south_west = Path(  # What is possible here: get big rusty key after making bunny search
    "Name placeholder",
    "A path South-West of the field.",
    "Monsters placeholder",
)

west_one = Path(  # What is possible here: well has water (obtain water) - obtain lighter fluid and matches and pot from somewhere, boil and get clean water
    "A large, unkept well lies in the middle of the path.",
    "A path West of the field.",
    "Monsters placeholder",
)
west_two = (
    Path(  # What is possible here: send bunny and get shiny key for portion of machine?
        "This path seems to be utterly filled with spruce trees, you cannot go in.",
        "A path West of the big well.",
        "Monsters placeholder",
    )
)

north_west = Path(  # What is possible here: unlock the gate with big rusty key gotten from South-West
    "There is a big gate here. It is locked.",
    "A path North-West of the field",
    "Monsters placeholder",
)
