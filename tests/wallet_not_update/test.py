import re

def test_wallet_not_update(client):
    """
    test pour savoir si les places sont bien retiré
    #issue 6
    """

    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    reg = r"Points available: ([0-9]+)"
    m = re.search(reg, response.data.decode())
    initial = int(m.group(1))-2 

    club = "Simply Lift"
    competition= "Testing"
    places = 2
    response = client.post('/purchasePlaces', data={"club": club, "competition" : competition, "places" : places})
    
    m2 = re.search(reg, response.data.decode())
    after = m2.group(1)
    assert int(after) == int(initial)