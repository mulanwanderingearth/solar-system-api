from app import create_app, db
from app.models.planet import Planet

my_app = create_app()

with my_app.app_context():
    planets = [
        Planet(name="Mercury", description="Water's planet", size= 10000,has_life= True),
        Planet(name="Jupiter", description="While", size=130000, has_life= False),
        Planet(name="Neptune", description="Black", size=4879534, has_life=False),
        Planet(name="Pluto", description="Blue", size=13356, has_life=False),
        
    ]

    db.session.add_all(planets)
    db.session.commit()