class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class GardenManager:
    def __init__(self, name: str, plants: list = None):
        if name is None or name == "":
            raise GardenError("Garden manager name cannot be empty!")
        self.name = name
        self.plants = plants if plants is not None else []

    def add_plant(self, plant: Plant) -> None:
        if plant.name is None or plant.name == "":
            raise GardenError("Cannot add a plant with an empty name!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(f"Error watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, water_level: int, sunlight_hours: int) -> None:
        if water_level < 1:
            raise GardenError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise GardenError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise GardenError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
            raise GardenError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        print(f"Plant '{self.name}' is healthy!\n")


def test_garden_manager():
    print("=== Garden Manager System ===\n")

    print("Adding plants to garden...")
    plant1 = Plant("tomato", 5, 6)
    plant2 = Plant("lettuce", 3, 4)
    plant3 = Plant("", 2, 3)
    manager = GardenManager("Garden Manager")
    try:
        manager.add_plant(plant1)
        manager.add_plant(plant2)
        manager.add_plant(plant3)
    except GardenError as e:
        print(f"Error adding plant: {e}\n")

    print("Watering plants...")
    try:
        manager.water()
    except GardenError as e:
        print(f"Error watering: {e}")


if __name__ == "__main__":
    test_garden_manager()