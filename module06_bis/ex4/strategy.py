from abc import ABC, abstractmethod

from ex3 import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    def _error(self, creature: Creature) -> InvalidStrategyError:
        return InvalidStrategyError(
            f"Invalid Creature '{creature.name}' for this "
            f"{self.name.lower()} strategy"
        )


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Normal")

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise self._error(creature)
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Aggressive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise self._error(creature)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
