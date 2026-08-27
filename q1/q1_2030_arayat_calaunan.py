class Car:
    def __init__(self,brand,model,battery=33):
        self.brand = brand
        self.model = model
        self.battery = battery
        distance = 0
    def go(self, distance):
        s = self.distance / 25
        battery -= self.battery - s
        print ("We traveled", distance, "km")
        print ("Your", self.brand, sel.model, self.battery, "wH left")
    def charge(self, wH):
        self.battery = self.battery + wH
        print("You charged", wH, "wH")
        print("You have", self.battery, "wH left" )
    
brand = input("What is the brand of your car?")
model = input("What is the model of your car?")
myCar = Car(brand, model)
while myCar.battery>0:
    command = input("What do you want to do? (go, charge)")
    if command == "go":
        distance = int(input("How far?"))
        myCar.go(distance)
    elif command == "charge":
        wH = int(input("How much?"))
        myCar.charge(wH)
    else:
        print("Invalid command")
print ("Your car ran out of battery")

