from tests.conftest import client

def test_display_clubs(client):
    """
    Feature for showing other clubs info
    #issue 7
    """
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    assert "Other clubs" in response.data.decode()
