from flask import Blueprint, Response, abort, make_response, request
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
    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name == name_param)
    
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    query =db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name == name_param).order_by(Planet.id)
    
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%")).order_by(Planet.id)

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

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {"id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size,
            "has_life": planet.has_life}

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"} 
        abort(make_response(response, 400))   

    query = db.select(Planet).where(Planet.id == planet_id)  
    planet = db.session.scalar(query)

    if not planet:
        not_found = {"message": f"planet {planet_id} not found"}
        abort(make_response(not_found, 404))

    return planet    

@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
    planet.has_life = request_body["has_life"]
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")

@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")