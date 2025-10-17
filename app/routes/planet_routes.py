from flask import Blueprint
from app.models.planet import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    result_list = []
    for planet in planets:
        result_list.append({
            "id": planet.id,
            "name": planet.name,
            "size": planet.size,
            "description": planet.description,
            "has_life": planet.has_life 
        })
    return result_list