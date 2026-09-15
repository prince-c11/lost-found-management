from app import app

def test_app_exists():
    assert app is not None

def test_login_page():
    client = app.test_client()
    response = client.get('/login')
    assert response.status_code == 200
