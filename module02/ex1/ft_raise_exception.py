MIN_TEMP = 0
MAX_TEMP = 40


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature > MAX_TEMP:
        raise ValueError(
            f"{temperature}°C is too hot for plants (max {MAX_TEMP}°C)")
    if temperature < MIN_TEMP:
        raise ValueError(
            f"{temperature}°C is too cold for plants (min {MIN_TEMP}°C)")
    return temperature


def test_temperature() -> None:
    test_inputs = ["25", "abc", "100", "-50"]
    for temp_str in test_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
