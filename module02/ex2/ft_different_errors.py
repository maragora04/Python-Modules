def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        file = open("/non/existent/file")
        file.close()
    elif operation_number == 3:
        result = "Height: " + 25  # type: ignore
        print(result)
    else:
        return


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            print("Operation completed successfully")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
