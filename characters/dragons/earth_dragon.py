from .dragon import Dragon

class EarthDragon(Dragon):
    
    name = 'Earth'
    implemented = True  # Change to True to view in the GUI
    food_cost = 4

    def __init__(self, armor = 4):
        self.armor = armor
    
