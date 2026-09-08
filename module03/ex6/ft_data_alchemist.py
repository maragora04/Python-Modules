import random


def game_data_alchemist() -> None:

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
                        "Gregory", "john", "kevin", "Liam", ]
    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    originally_capitalized = [
        name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {originally_capitalized}")

    scores = {name: random.randint(1, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    avg_score = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg_score}")

    high_score = {
        name: score for name, score in scores.items() if score > avg_score}
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    game_data_alchemist()
