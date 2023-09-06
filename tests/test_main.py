import pytest
from page_analyzer import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_main_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Анализатор страниц' in response.data.decode('utf-8')
    assert 'Сайты' in response.data.decode('utf-8')
