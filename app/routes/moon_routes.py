from flask import Response, abort, make_response, Blueprint, request
from ..models.moon import Moon
from ..db import db
from .routes_utilities import validate_model

bp = Blueprint("moon_bp", __name__, url_prefix="/moons")


@bp.get("/<int:id>")
def get_some_moon(id):
    moon = validate_model(id)

    return moon.to_dict(), 200
