class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Player(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Monster(Entity):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength
