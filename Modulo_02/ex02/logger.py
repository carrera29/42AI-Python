import time
from random import randint
import os

def log(original_funtion):
    def decorador(*args, **kwargs):
        user = str(os.getlogin)
        start = time.time()
        result = original_funtion(*args, **kwargs)
        end = time.time()
        if original_funtion.__name__ is "make_coffee":
            msg = (f"""({user})Running: {original_funtion.__name__}    [ exec-time = {end - start:.3f} s  ]""")
        else:
            msg = (f"""({user})Running: {original_funtion.__name__}    [ exec-time = {end - start:.3f} ms ]""")
        with open ("machine", "a") as f:
            print (msg, file=f)
        return result
    return decorador

    
class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()

for i in range(0, 5):
    machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)