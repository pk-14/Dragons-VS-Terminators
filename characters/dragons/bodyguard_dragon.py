from .container_dragon import ContainerDragon


class BodyguardDragon(ContainerDragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    food_cost = 4
    is_container = True
    implemented = True  # Change to True to view in the GUI
    
    def __init__(self, armor=2):
        ContainerDragon.__init__(self, armor)
        self.contained_dragon = None
        
    # END 3.2
