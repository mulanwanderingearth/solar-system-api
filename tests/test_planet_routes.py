def test_get_all_planets_with_no_records(client):

    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeds(client, one_planet):

    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "Water's planet",
        "size": 10000,
        "has_life": True
    }

def test_create_one_planet(client):
    #Act
    response = client.post("/planets", json={
        "name": "Venus",
        "description": "Girl's planet",
        "size": 20000,
        "has_life": True
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "Girl's planet",
        "size": 20000,
        "has_life": True
    }
