class Plant:
    def __init__(self, name: str, age: int, status: str, water_tank: int = 10):
        self.name = name
        self.status = status
        self.age = age
        self.water_tank = water_tank

    def water(self, amount: int) -> None:
        if amount < self.water_tank:
            pass
        else:
            print(f"{self.name} is happy with {amount}l of water!\n")


def water_plants(plants_list: list):
    print("Opening watering system")
    for plant in plants_list:
        try:
            if plant.water_tank < 5:
                raise ValueError(f"{plant.name} needs more water!")
            else:
                print(
                    f"{plant.name} has {plant.water_tank}l of water!",
                    end="\n\n")
        except ValueError as e:
            print(f"Caught an error: {e}")
        finally:
            print(f"Finished watering {plant.name}\n")
