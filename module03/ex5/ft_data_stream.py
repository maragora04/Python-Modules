import random
from typing import Generator, List, Tuple

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "eat", "sleep", "grab", "move", "swim", "climb", "use",
    "release", ]


def gen_event() -> Generator[Tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    event_list: List[Tuple[str, str]]
) -> Generator[Tuple[str, str], None, None]:
    while event_list:
        index = random.randrange(len(event_list))
        yield event_list.pop(index)


def events() -> None:

    stream = gen_event()
    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    events()
