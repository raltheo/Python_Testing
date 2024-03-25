def test_buying_more_than_12(client):
    """
    test pour vérifier qu'on ne peut pas buy plus de place que 12
    # issue 4
    """

    club = "Simply Lift"
    competition= "Spring Festival"
    places = 13
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})

    assert 'Great-booking complete!' not in response.data.decode()