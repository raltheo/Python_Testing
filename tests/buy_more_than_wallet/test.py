from tests.conftest import client
import re

def test_buying_more_than_wallet(client):
    """
    test pour vérifier qu'on ne peut pas buy plus de place que notre solde
    # issue 2
    """
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    reg = r"Points available: ([0-9]+)"
    m = re.search(reg, response.data.decode())
    to_buy = int(m.group(1))+1

    club = "Simply Lift"
    competition= "Spring Festival"
    places = to_buy
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})

    assert 'Great-booking complete!' not in response.data.decode()