class Car(object):
    """
        blueprint for car
    """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def __repr__(self):
        return "%s %s %s %s" % (self.model, self.color, self.company, self.speed_limit)

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

print(suzuki)
print(audi)

audi.accelarate()