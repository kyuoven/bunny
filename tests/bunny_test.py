from nose.tools import *
from bunny import bunny
from bunny.adventure_with_bunny import Path

# this is what copilot added
def test_bunny():
    assert (bunny.name, "A name")
    assert (bunny.color, "White")
    assert (
        bunny.description,
        """
    A White rabbit with red eyes
    """,
    )
    assert (bunny.personality, "Personality is timid, shy and reserved")
    assert (bunny.ability, "Ability placeholder")


# end copilot


def test_room():
    carrots = Path(
        "Carrot Test room",
        """This room has a lot of fresh, juicy carrots.""",
    )
    assert (carrots.name, "Carrot Test room")
    assert (carrots.paths, {})


def test_room_paths():
    Middle = Path("Center", "Test room in the center.")
    right = Path("Right", "Test room on the right.")
    left = Path("Left", "Test room on the left.")
    middle = Path("Middle", "Test room in the middle.")

    Middle.add_paths({"right": right, "left": left, "middle": middle})
    assert (Middle.go("right"), right)
    assert (Middle.go("left"), left)
    assert (Middle.go("middle"), middle)


def test_map():
    start = Path("Start", "You can go to the left, middle and right.")
    left = Path("Left", "Djungelskog is here.")
    middle = Path("Middle", "You are trapped here with Elon Musk")
    right = Path("Right", "It's dark, and there is an imposter here")

    start.add_paths({"left": left, "middle": middle, "right": right})
    left.add_paths({"back": start})
    middle.add_paths({"back": start})
    right.add_paths({"back": start})

    assert (start.go("left"), left)
    assert (start.go("middle").go("back"), start)
    assert (start.go("right").go("back"), start)
