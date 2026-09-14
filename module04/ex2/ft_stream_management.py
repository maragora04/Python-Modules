import sys


def get_user_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line = sys.stdin.readline()
    return line.rstrip("\r\n").strip()


def transform_content(content: str) -> str:
    lines = content.splitlines()
    transformed_lines = [f"{line}#" for line in lines]
    return "\n".join(transformed_lines)


def save_content(content: str) -> None:
    new_filename = get_user_input("Enter new file name (or empty): ")

    if not new_filename:
        print("Data not saved")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        with open(new_filename, "w") as file:
            file.write(content)
        print(f"Data saved in file '{new_filename}'")
    except Exception as err:
        sys.stderr.write(f"Error opening file '{new_filename}': {err}")
        print("Data not saved")


def read_filename() -> None:
    filename = sys.argv[1]
    try:
        file = open(filename, "r")
        content = file.read()
        print(f"Accessing file '{filename}'")
        print("---\n")
        print(f"{content}\n")
        print("---\n")
        file.close()
        print(f"File '{filename}' closed.")

        transformed = transform_content(content)
        print("Transform data:")
        print("---\n")
        print(f"{transformed}\n")
        print("---\n")

        save_content(transformed)

    except Exception as err:
        sys.stderr.write(f"Error opening file '{filename}': {err}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    arg_len = len(sys.argv)
    if arg_len < 2:
        print("No filename provided")
    elif arg_len > 2:
        print("Only one text file can be read at a time!")
        print(f"Reading first filename passed: '{sys.argv[1]}'")
        read_filename()
    else:
        read_filename()
