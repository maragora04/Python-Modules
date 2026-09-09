#!/usr/bin/env python3

import random

ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder", "Night Owl", "Lucky Star",
    "Iron Will", "Completionist", "Legend of the Realm",
    "Pixel Perfectionist", ]


def player_achievements() -> set[str]:
    nb_achievements = random.randint(10, 15)
    player_achvs = set(random.sample(ACHIEVEMENTS, nb_achievements))
    return player_achvs


def print_players(players) -> None:
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")


def print_only(players) -> None:
    for name, achievements in players.items():
        others = [
            achv for other, achv in players.items() if other != name]
        only_mine = achievements.difference(*others)
        print(f"Only {name} has: {only_mine}")


def print_missing(players) -> None:
    for name, achievements in players.items():
        missing = set(ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}")


def gen_player_achievements() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": player_achievements(),
        "Bob": player_achievements(),
        "Charlie": player_achievements(),
        "Dylan": player_achievements(), }

    print_players(players)

    all_sets = list(players.values())
    all_distinct = all_sets[0].union(*all_sets[1:])
    print(f"All distinct achievements: {all_distinct}")

    common = all_sets[0].intersection(*all_sets[1:])
    print(f"Common achievements: {common}")

    print_only(players)
    print_missing(players)


if __name__ == "__main__":
    gen_player_achievements()
