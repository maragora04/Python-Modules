from ex3 import Creature, TransformCapability, TransformCreatureFactory


def test_creature(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    print(" base:")
    test_creature(factory.create_base())
    print(" evolved:")
    test_creature(factory.create_evolved())


if __name__ == "__main__":
    main()
