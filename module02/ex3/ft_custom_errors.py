class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_supply() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError...")
    try:
        check_water_supply()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")
    for operation in (check_plant_health, check_water_supply):
        try:
            operation()
        except GardenError as error:
            print(f"Caught GardenError: {error}")

    print("All custom error types work correctly")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
