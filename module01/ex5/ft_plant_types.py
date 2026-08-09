class Plant:
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 1.0,
    ) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = growth_rate
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

    def grow(self) -> None:
        self.set_height(round(self._height + self._growth_rate, 1))

    def age_up(self) -> None:
        self.set_age(self._age + 1)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 1.0,
        color: str = "unknown",
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 1.0,
        trunk_diameter: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 1.0,
        harvest_season: str = "unknown",
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age_up(self) -> None:
        super().age_up()
        self._nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, color="red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, trunk_diameter=5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable(
        "Tomato", 5.0, 10, growth_rate=2.1, harvest_season="April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()
