class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 1.0,
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
    plants = [
        Plant("Rose", 25.0, 30, growth_rate=0.8),
        Plant("Oak", 200.0, 365, growth_rate=0.3),
        Plant("Cactus", 5.0, 90, growth_rate=0.05),
        Plant("Sunflower", 80.0, 45, growth_rate=2.5),
        Plant("Fern", 15.0, 120, growth_rate=0.6),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
