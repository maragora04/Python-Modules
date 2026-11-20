from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory_a: CreatureFactory,
                factory_b: CreatureFactory) -> None:
    print("Testing battle")
    fighter_a = factory_a.create_base()
    fighter_b = factory_b.create_base()
    print(fighter_a.describe())
    print(" vs.")
    print(fighter_b.describe())
    print(" fight!")
    print(fighter_a.attack())
    print(fighter_b.attack())


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()

    test_factory(flame)
    print()
    test_factory(transform)
    print()
    test_battle(flame, transform)

if __name__ == "__main__":
    main()
