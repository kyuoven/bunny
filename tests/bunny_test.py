from nose.tools import *
from bunny import bunny
from bunny.adventure_with_bunny import Path


def test_room():
    carrots = Path(
        "Carrot Test room",
        """This room has a lot of fresh, juicy carrots.""",
    )
    assert (carrots.name, "Carrot Test room")
    assert (carrots.paths, {})


def test_room_paths():
    Middle = Path("Middle", "Test room in the middle.")
    North = Path("Noth", "Test room in the North.")
    NorthEast = Path("North-East", "Test room in the North-East.")
    East = Path("East", "Test room in the East.")
    SouthEast = Path("South-East", "Test room in the South-East.")
    South = Path("South", "Test room in the South.")
    SouthWest = Path("South-West", "Test room in the South-West.")
    West = Path("West", "Test room in the West.")
    NorthWest = Path("North-West", "Test room in the North-West.")
    UpperNorth = Path("Upper North", "Test room in the Upper North.")
    UpperEast = Path("Upper East", "Test room in the Upper East.")
    UpperSouth = Path("Upper South", "Test room in the Upper South.")
    UpperWest = Path("Upper West", "Test room in the Upper West.")

    Middle.add_paths(
        {
            "North": North,
            "NorthEast": NorthEast,
            "East": East,
            "SouthEast": SouthEast,
            "South": South,
            "SouthWest": SouthWest,
            "West": West,
            "NorthWest": NorthWest,
            "UpperNorth": UpperNorth,
            "UpperEast": UpperEast,
            "UpperSouth": UpperSouth,
            "UpperWest": UpperWest,
        }
    )
    assert (Middle.go("North"), North)
    assert (Middle.go("NorthEast"), NorthEast)
    assert (Middle.go("East"), East)
    assert (Middle.go("SouthEast"), SouthEast)
    assert (Middle.go("South"), South)
    assert (Middle.go("SouthWest"), SouthWest)
    assert (Middle.go("West"), West)
    assert (Middle.go("NorthWest"), NorthWest)
    assert (Middle.go("UpperNorth"), UpperNorth)
    assert (Middle.go("UpperEast"), UpperEast)
    assert (Middle.go("UpperSouth"), UpperSouth)
    assert (Middle.go("UpperWest"), UpperWest)


def test_map():
    Middle = Path("The Middle", "There is a big field here, surrounded by flowers.")
    North = Path("It's full of Spruce trees.")
    NorthEast = Path(
        "North-East path", "There's a shallow hole in the ground, the size of you."
    )
    East = Path("East path", "There's a machine overgrown with moss.")
    SouthEast = Path("South-East path", "Filled with traps - Be careful!")
    South = Path("South path", "There's a nice pond here")
    SouthWest = Path("South-West path", "Overgrown, but bunny can go through and look.")
    West = Path("West path", "A large, unkept well lies in the middle of the path.")
    NorthWest = Path(
        "North-West path",
        "There is a big gate here, maybe it'll open with the right key.",
    )
    UpperNorth = Path("Upper North path", "An old camp lays abandoned here.")
    UpperEast = Path("Upper East path", "There is an old hospital here.")
    UpperSouth = Path("Upper South path", "You can hear the sound of bees.")
    UpperWest = Path("Upper West path", "This area is not reachable.")

    Middle.add_paths(
        {
            "North": North,
            "NorthEast": NorthEast,
            "East": East,
            "SouthEast": SouthEast,
            "South": South,
            "SouthWest": SouthWest,
            "West": West,
            "NorthWest": NorthWest,
            "UpperNorth": UpperNorth,
            "UpperEast": UpperEast,
            "UpperSouth": UpperSouth,
            "UpperWest": UpperWest,
        }
    )
    North.add_paths({"Back": Middle})
    NorthEast.add_paths({"Back": Middle})
    East.add_paths({"Back": Middle})
    SouthEast.add_paths({"Back": Middle})
    South.add_paths({"Back": Middle})
    SouthWest.add_paths({"Back": Middle})
    West.add_paths({"Back": Middle})
    NorthWest.add_paths({"Back": Middle})
    UpperNorth.add_paths({"Back": North})
    UpperEast.add_paths({"Back": East})
    UpperSouth.add_paths({"Back": South})
    UpperWest.add_paths({"Back": West})

    assert (Middle.go("North").go("back"), Middle)
    assert (Middle.go("NorthEast"), Middle)
    assert (Middle.go("East").go("back"), Middle)
    assert (Middle.go("SouthEast").go("back"), Middle)
    assert (Middle.go("South"), Middle)
    assert (Middle.go("SouthWest").go("back"), Middle)
    assert (Middle.go("West").go("back"), Middle)
    assert (Middle.go("NorthWest").go("back"), Middle)
    assert (Middle.go("UpperNorth").go("back"), Middle)
    assert (Middle.go("UpperEast").go("back"), Middle)
    assert (Middle.go("UpperSouth").go("back"), Middle)
    assert (Middle.go("UpperWest").go("back"), Middle)
