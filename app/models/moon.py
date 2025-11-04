from ..db import db
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .planet import Planet

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[int]
    description: Mapped[Optional[str]]
    has_life: Mapped[bool] = mapped_column(default=False)
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "has_life": self.has_life,
            "planet": self.planet.name if self.planet_id else None
        }
    
    @classmethod
    def from_dict(cls, moon_data):
        return cls(
        name=moon_data["name"],
        size=moon_data["size"],
        description=moon_data.get("description"),
        has_life=moon_data.get("has_life", False),
        planet_id=moon_data.get("planet_id")
    )
