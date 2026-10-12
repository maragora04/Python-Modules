import alchemy

def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print()
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="", flush=True)
    try:
        print(f"{alchemy.create_earth()}")  # type: ignore
    except AttributeError as error:
        print(f"\nCaught: {error}")


if __name__ == "main":
    main()

# delete the typeignore later
