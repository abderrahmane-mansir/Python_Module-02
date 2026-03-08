def garden_operations(error_type: str = "") -> None:
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        print(1 / 0)
    elif error_type == "file":
        file = open("missing.txt", "r")
        file.close()
    elif error_type == "key":
        garden = {"plant": "tomato"}
        print(garden["missing_plant"])
    else:
        int("abc")
        print(1 / 0)
        file = open("missing.txt", "r")
        file.close()
        garden = {"plant": "tomato"}
        print(garden["missing_plant"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===", end="\n\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()", end="\n\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero", end="\n\n")
    else:
        print("Execution successful", end="\n\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as error:
        print(
            f"Caught FileNotFoundError: No such file '{error.filename}'",
            end="\n\n"
        )
    else:
        print("Execution successful", end="\n\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as error:
        print(
            f"Caught KeyError: Missing key: {error}", end="\n\n"
        )
    else:
        print("Execution successful", end="\n\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("file")
    except Exception:
        print("Caugh an error, but program continues!", end="\n\n")
    else:
        print("Execution successful", end="\n\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
