from app import app

def test_app_exists():
    assert app is not None

def test_login_page():
    client = app.test_client()
    response = client.get('/login')
    assert response.status_code == 200

def test_add_item_requires_login():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.get('/add_item')

    assert response.status_code == 302
