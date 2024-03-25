from tests.conftest import client

def test_display_clubs(client):
    """
    Feature for showing other clubs info
    #issue 7
    """
    response = client.get('/displayclubs')
    assert "Clubs" in response.data.decode()
