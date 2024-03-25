def test_buy_more_place_available(client):
    """
    test pour vérifier qu'on ne peut pas acheter plus de place qu'il ya de disponible
    # issue je sais pas combien xD
    """

    club = "Simply Lift"
    competition= "VIP_Event"
    places = 5
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})

    assert 'Great-booking complete!' not in response.data.decode()