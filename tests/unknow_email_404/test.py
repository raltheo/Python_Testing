from tests.conftest import client

def test_unknow_email_404(client):
    """
    Entering a unknown email crashes the app
    #issue 1
    """
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    assert response.status_code == 200 
    email = "test@example.com"
    response = client.post('/showSummary', data={"email": email})
    assert response.status_code == 404