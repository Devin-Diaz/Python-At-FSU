'''
Design a Ship class with the following members: (20)
    ▪ A field for the name of the ship
    ▪ A field for the year that the ship was built
    ▪ An initializer method that accepts two arguments to initialize the two fields
    ▪ A __str__ method that returns the object's state as a string
Design a CruiseShip class that is a subclass of the Ship class. The CruiseShip class should have the
following members:
    ▪ A field for the maximum number of passengers
    ▪ An initializer method that accepts three arguments to initialize the three fields
    ▪ A __str__ method that returns the object's state as a string
Design a CargoShip class that is a subclass of the Ship class. The CargoShip class should have the
following members:
    ▪ A field for the cargo capacity in tonnage
    ▪ An initializer method that accepts three arguments to initialize the three fields
    ▪ A __str__ method that returns the object's state as a string
Demonstrate polymorphism in a test program by creating related objects (all three Ship types) and
passing the objects to a function for printing their details (by implicitly calling the __str__ method).
'''

# parent class
class Ship:
    def __init__(self, ship_name: str = None, year_built: int = None) -> None:
        self.ship_name = ship_name
        self.year_built = year_built
        
    def initialize_ship_data(self, ship_name: str, year_built: int):
        self.ship_name = ship_name
        self.year_built = year_built
    
    def __str__(self):
        return f'Regular ship: [ {self.ship_name}, {self.year_built} ]'

# child class
class CruiseShip(Ship):
    def __init__(self, ship_name: str = None, year_built: int = None, max_passengers: int = None) -> None:
        super().__init__(ship_name, year_built)
        self.num_passengers = max_passengers

    def initialize_ship_data(self, ship_name: str, year_built: int, max_passengers: int):
        self.ship_name = ship_name
        self.year_built = year_built
        self.max_passengers = max_passengers
    
    def __str__(self):
        return f'Cruise Ship: [ {self.ship_name}, {self.year_built}, {self.num_passengers} ]'

# child class
class CargoShip(Ship):
    def __init__(self, ship_name: str = None, year_built: int = None, cargo_capacity: int = None) -> None:
        super().__init__(ship_name, year_built)
    
    def initialize_ship_data(self, ship_name: str, year_built: int, cargo_capacity: int):
        self.ship_name = ship_name
        self.year_built = year_built
        self.cargo_capacity = cargo_capacity
    
    def __str__(self):
        return f'Cargo Ship: [ {self.ship_name}, {self.year_built}, {self.cargo_capacity} ]'

# iterates through all instances of types of ships created
def display_ship_data(all_ships: list[Ship]):
    for ship in all_ships:
        print(ship)

# creating ships
ship = Ship()
ship.initialize_ship_data('Cool Ship', 2024)

cruise = CruiseShip()
cruise.initialize_ship_data('Party Ship', 2025, 500)

cargo = CargoShip()
cargo.initialize_ship_data('Work Ship', 2026, 1000)

all_ships = [ship, cruise, cargo]

# begins program
display_ship_data(all_ships)
