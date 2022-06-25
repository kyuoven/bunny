# this file is like player.py


class Position(object):
    def __init__(self, title, options):
        self.title = title
        self.options = options


class bunny(object):
    def __init__(self, name, color, description, personality, ability):
        self.name = name
        self.color = color
        self.description = description
        self.personality = personality
        self.ability = ability


One = Position(
    "Choose your companion",
    ">A (Mochi) \n >B (Snowflake) \n >C (Bugs)",
)

A = bunny(
    "A name",
    "White",
    """
    A White rabbit with red eyes
    """,
    "Personality is timid, shy and reserved",
    "Ability placeholder",
)
B = bunny(
    "A name",
    "Grey",
    """
    A placeholder
    """,
    "A personality placeholder",
    "Ability placeholder",
)
C = bunny(
    "A name",
    "Grey",
    """
    A placeholder
    """,
    "A personality placeholder",
    "Ability placeholder",
)
