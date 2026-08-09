class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    new_height = 25
    if rose.set_height(new_height):
        print(f"Height updated: {new_height}cm")
    else:
        print("Height update rejected")

    new_age = 30
    if rose.set_age(new_age):
        print(f"Age updated: {new_age} days")
    else:
        print("Age update rejected")

    bad_height = -10
    if rose.set_height(bad_height):
        print(f"Height updated: {bad_height}cm")
    else:
        print("Height update rejected")

    bad_age = -5
    if rose.set_age(bad_age):
        print(f"Age updated: {bad_age} days")
    else:
        print("Age update rejected")

    print("Current state: ", end="")
    rose.show()
