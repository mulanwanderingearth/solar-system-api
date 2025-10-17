class Planet():
    def __init__(self, id, name, description, size, has_life):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
        self.has_life = has_life

planets =[
    Planet(1, "Mars", "red planet", "6000 km", False),
    Planet(2, "Venus", "girl's planet", "10000 km", False),
    Planet(3, "Earth", "water planet", "16000 km", True)
]