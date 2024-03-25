def test_buying_place_past_competition(client):
    """
    test pour vérifier qu'on ne peut pas acheter dans des compétitions deja passé
    # issue 5
    """
    
    club = "Simply Lift"
    competition= "Spring Festival"
    places = 1
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})

    assert 'Great-booking complete!' not in response.data.decode()

    club = "Simply Lift"
    competition= "Testing"
    places = 1
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})

    assert 'Great-booking complete!' in response.data.decode()