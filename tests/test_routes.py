import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING!] = True
    with app.test_client() as client: 
        yield client

def test_index(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert json_data['message'] == 'Hello, World!
