from elements import create_fire
from alchemy import elements
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
        f"and '{strength_potion()}' "
        f"mixed with '{create_fire()}'")
