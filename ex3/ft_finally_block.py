class Plant:
    def __init__(self, name: str, age: int, water_tank: int = 10) -> None:
        self.name = name
        self.age = age
        self.water_tank = water_tank

    def water(self) -> None:
        if self.name is None or self.name == "":
            raise ValueError(f"Cannot water {self.name} - invalid plant!")
        print(f"Watering {self.name}")


def water_plants(plants_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants_list:
            plant.water()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    plants = [
        Plant("tomato", 2, 3),
        Plant("lettuce", 1, 4),
        Plant("carrots", 3, 1)
    ]
    print("Testing normal watering...")
    try:
        water_plants(plants)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as error:
        print(f"Unexpected Error: {error}")
    finally:
        print("Watering complete successfully!\n")

    print("Testing with error...")
    plants_with_error = [
        Plant("tomato", 1, 6),
        Plant(None, 2, 3),
    ]
    try:
        water_plants(plants_with_error)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as error:
        print(f"Unexpected Error: {error}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
