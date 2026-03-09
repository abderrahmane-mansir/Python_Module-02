class Plant:
    def __init__(self, name: str, age: int,
                 status: str, water_tank: int) -> None:
        self.name = name
        self.status = status
        self.age = age
        self.water_tank = water_tank

    def set_status(self, status: str) -> None:
        self.status = status
        if status not in ["healthy", "wilting"]:
            raise ValueError("Invalid status. Must be 'healthy' or 'wilting'")
        if status == "wilting":
            raise PlantError(self)

    def water(self, amount: int) -> None:
        if amount < self.water_tank:
            raise WaterError(amount)
        else:
            print(f"{self.name} is happy with {amount}l of water!\n")


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: Plant) -> None:
        super().__init__(f"The {plant.name} plant is wilting")


class WaterError(GardenError):
    def __init__(self, water: int) -> None:
        super().__init__("Not enough water in the tank!\n")


def test_plant_error(plant: Plant) -> None:
    try:
        plant.set_status("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def test_water_error(plant: Plant) -> None:
    try:
        plant.water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_errors(plant: Plant) -> None:
    try:
        plant.set_status("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        plant.water(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    plant = Plant("tomato", 1, "healthy", 10)
    print("=== Custom Garden Errors Demo ===", end="\n\n")

    print("Testing PlantError...")
    test_plant_error(plant)
    print("Testing WaterError...")
    test_water_error(plant)
    print("Testing catching all garden errors...")
    test_all_errors(plant)
    print("All custom error types work correctly!")
