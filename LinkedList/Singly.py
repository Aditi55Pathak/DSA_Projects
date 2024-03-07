# A rollar coaster where it have each car one after another


class Car:
    def __init__(self, car_id, num_passengers):
        self.car_id = car_id
        self.num_passengers = num_passengers
        self.next = None


class Train:
    def __init__(self):
        self.head = None

    def add_car(self, car):
        if not self.head:
            self.head = car
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = car

    def remove_car(self):
        if not self.head:
            print("Train is empty.")
            return None
        removed_car = self.head
        self.head = self.head.next
        return removed_car


class RollerCoaster:
    def __init__(self):
        self.train = Train()

    def load_train(self, car):
        self.train.add_car(car)
        print(f"Car {car.car_id} loaded with {car.num_passengers} passengers.")

    def unload_train(self):
        removed_car = self.train.remove_car()
        if removed_car:
            print(f"Car {removed_car.car_id} unloaded with {removed_car.num_passengers} passengers.")

    def run(self):
        print("Roller coaster running.")
        current = self.train.head
        while current:
            print(f"Moving car {current.car_id} with {current.num_passengers} passengers.")
            current = current.next
        print("Roller coaster completed its run.")


if __name__ == "__main__":
    roller_coaster = RollerCoaster()

    # Load cars
    roller_coaster.load_train(Car(1, 4))
    roller_coaster.load_train(Car(2, 3))
    roller_coaster.load_train(Car(3, 5))

    # Run roller coaster
    roller_coaster.run()

    # Unload cars
    roller_coaster.unload_train()
    roller_coaster.unload_train()
    roller_coaster.unload_train()