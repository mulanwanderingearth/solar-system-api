from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]
    has_life = request_body["has_life"]
    

    new_planet = Planet(
        name=name,
        description=description,
        size=size,
        has_life=has_life 
    )

    db.session.add(new_planet)
    db.session.commit()

    planet_response = dict(
        id=new_planet.id,
        name=new_planet.name,
        description=new_planet.description,
        size=new_planet.size,
        has_life=new_planet.has_life,
    )
    
    return planet_response, 201

@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    result_list = []

    for planet in planets:
        result_list.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size,
            "has_life": planet.has_life
        })

    return result_list

