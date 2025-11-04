from flask import abort, make_response
from ..db import db

def validate_model(cls, id):
    try:
        id = int(id)
    except:
        response = {"message": f"{cls.__name__} id {id} invalid"} 
        abort(make_response(response, 400))   

    query = db.select(cls).where(cls.id == id)  
    model = db.session.scalar(query)

    if not model:
        not_found = {"message": f"{cls.__name__} id {id} not found"}
        abort(make_response(not_found, 404))

    return model

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201