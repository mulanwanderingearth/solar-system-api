from flask import Blueprint, Response, abort, make_response, request
from app.models.planet import Planet
from ..db import db
from .routes_utilities import validate_model

bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    # new_planet = Planet.from_dict(request_body)
    try:
        new_planet = Planet.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()
    
    return new_planet.to_dict(), 201

@bp.get("")
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
        result_list.append(planet.to_dict())

    return result_list

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict(), 200



@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
    planet.has_life = request_body["has_life"]
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")

@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")