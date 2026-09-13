class Glassware:
    def __init__(self, material="glass"):
        self.material = material

    def display_info(self):
        print(f"Material: {self.material}")


class Beaker(Glassware):
    def __init__(self, capacity, material="glass"):
        super().__init__(material)
        self.capacity = capacity

    def display_info(self):
        print(
            f"Beaker - Capacity: {self.capacity} mL, "
            f"Material: {self.material}"
        )


class Tray:
    def __init__(self):
        self.__beakers = [
            Beaker(100),
            Beaker(150),
            Beaker(200),
            Beaker(250),
            Beaker(500)
        ]

    def display_beakers(self):
        for i, beaker in enumerate(self.__beakers, start=1):
            print(f"Beaker {i}:")
            beaker.display_info()

    def __del__(self):
        self.__beakers.clear()


if __name__ == "__main__":
    tray = Tray()

    print("Tray inventory:")
    tray.display_beakers()

    del tray
