from flask import Blueprint, abort, make_response
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

def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except ValueError:
        invalid_response = {"message": f"Planet id {planet_id} is invalid. Must be an integer."} 
        abort(make_response(invalid_response, 400))   

    for planet in planets:
        if planet.id == planet_id:
            return planet

    not_found_response = {"message": f"Planet id {planet_id} not found"} 
    abort(make_response(not_found_response, 404))

@planet_bp.get("/<planet_id>")
def get_single_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "size": planet.size,
        "description": planet.description,
        "has_life": planet.has_life
    }

