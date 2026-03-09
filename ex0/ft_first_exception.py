#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    print("Testing temperature: ", temp_str)
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(
            f"{temp_str}°C is too cold for plants (min 0°C)"
            )
    elif temp > 40:
        raise ValueError(
            f"{temp_str}°C is too hot for plants (max 40°C)"
            )
    else:
        return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    for value in ["25", "abc", "100", "-50"]:
        try:
            temp = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants!\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
