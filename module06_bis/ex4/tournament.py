from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    fighters = [(f.create_base(), s) for f, s in opponents]
    labels = ", ".join(f"({c.name}+{s.name})" for c, s in fighters)
    print(f" [ {labels} ]")
    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved")
    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                c1, s1 = fighters[i]
                c2, s2 = fighters[j]
                print("\n* Battle *")
                print(c1.describe())
                print(" vs.")
                print(c2.describe())
                print(" now fight!")
                s1.act(c1)
                s2.act(c2)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame, normal), (transform, aggressive)])

    print("\nTournament 1 (error)")
    battle([(transform, aggressive), (flame, aggressive)])


if __name__ == "__main__":
    main()
