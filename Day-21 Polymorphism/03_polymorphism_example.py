class Bird:

    def fly(self):
        print("Bird is flying")

class Airplane:

    def fly(self):
        print("Airplane is flying")

def start_flying(obj):
    obj.fly()

bird = Bird()
plane = Airplane()

start_flying(bird)
start_flying(plane)

# The same function works with different objects because both provide a fly() method.