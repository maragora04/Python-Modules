class Plant:
    YEAR_IN_DAYS = 365

    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

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
        self._stats: "Plant.Stats" = self.Stats()
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant.Stats":
        return self._stats

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
        self._stats.record_grow()
        self.set_height(round(self._height + self._growth_rate, 1))

    def age_up(self, days: int = 1) -> None:
        self._stats.record_age()
        self.set_age(self._age + days)

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > Plant.YEAR_IN_DAYS

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

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
        self._stats.record_shade()
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

    def age_up(self, days: int = 1) -> None:
        super().age_up(days)
        self._nutritional_value += 0.5


class Seed(Flower):
    SEEDS_PER_BLOOM: int = 42

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 1.0,
        color: str = "unknown",
    ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = self.SEEDS_PER_BLOOM


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_a_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, growth_rate=8.0, color="red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, trunk_diameter=5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed(
        "Sunflower", 80.0, 45, growth_rate=30.0, color="yellow"
    )
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("=== Anonymous")
    mystery = Plant.create_anonymous()
    mystery.show()
    display_stats(mystery)
