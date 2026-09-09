import sys


def get_filename() -> None:
    filename = sys.argv[1]
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Cannot open file: permission denied")


if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len < 2:
        print("No filename provided")
    else:
        get_filename()
