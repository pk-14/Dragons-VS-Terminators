from .thrower_dragon import ThrowerDragon

class ScubaThrower(ThrowerDragon):
    name = 'Scuba'
    implemented = True  # Change to True to view in the GUI
    food_cost = 6
    is_watersafe = True
