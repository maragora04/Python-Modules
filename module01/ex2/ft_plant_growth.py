class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age_up(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, growth_rate=0.8)

    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_up()
        rose.show()

    week_increase = round(rose.height - initial_height, 1)
    print(f"Growth this week: {week_increase}cm")
