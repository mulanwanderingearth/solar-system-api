# class Planet():
#     def __init__(self, id, name, description, size, has_life):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size
#         self.has_life = has_life

# planets =[
#     Planet(1, "Mars", "red planet", "6000 km", False),
#     Planet(2, "Venus", "girl's planet", "10000 km", False),
#     Planet(3, "Earth", "water planet", "16000 km", True)
# ]

from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[int]
    has_life: Mapped[bool]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size,
            "has_life": self.has_life
        }
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(name=planet_data["name"],
                   description= planet_data["description"],
                   size=planet_data["size"],
                   has_life=planet_data["has_life"])


