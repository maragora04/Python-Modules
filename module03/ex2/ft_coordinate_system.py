import math


def get_coords(prompt: str) -> tuple:
    while True:
        coords = input(prompt)
        parts = coords.split(",")
        try:
            x, y, z = [float(i) for i in parts]
            return x, y, z
        except ValueError:
            print("Invalid syntax")


def distance_finder(one: tuple, two: tuple) -> float:
    dx = two[0] - one[0]
    dy = two[1] - one[1]
    dz = two[2] - one[2]
    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    return distance


def get_player_pos() -> None:

    print("Get a first set of coordinates")

    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    coords1 = get_coords(prompt)
    distance1 = math.sqrt(coords1[0]**2 + coords1[1]**2 + coords1[2]**2)
    print(f"Got a first tuple: {coords1}")
    print(f"It includes: X= {coords1[0]}, Y= {coords1[1]}, Z= {coords1[2]}")
    print(f"Distance to center: {distance1:.4f}")

    print("Get a second set of coordinates")
    coords2 = get_coords(prompt)
    distance2 = distance_finder(coords1, coords2)
    print(f"Distance between the 2 sets of coordinates: {distance2:.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
