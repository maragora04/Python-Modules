from typing import Tuple


def secure_archive(
    filename: str, action: str = "", content_to_write: str = ""
) -> Tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as file:
                content = file.read()
            return (True, f"'{content}'")
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content_to_write)
            return (True, "'Content successfully written to file'")
        else:
            return (False, f"Invalid action: '{action}'")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"), "\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("etc/master.passwd", "read"), "\n")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read")
    print(result, "\n")

    print("Using 'secure_archive' to write previous content to a new file:")

    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1],))
