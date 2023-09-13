import pytest
from page_analyzer import app
from page_analyzer.psql_db import drop_all, execute_sql_script


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            execute_sql_script()
        yield client
    with app.app_context():
        drop_all()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Анализатор страниц' in response.data.decode('utf-8')
    assert 'Сайты' in response.data.decode('utf-8')


def test_valid_url(client):
    response = client.post('/urls', data={'url': 'https://ru.hexlet.io/'})
    assert response.status_code == 302
    with client.session_transaction() as session:
        flash_messages = session['_flashes']
        assert flash_messages
        assert 'Страница успешно добавлена' in flash_messages[0]


def test_invalid_url(client):
    response = client.post('/urls', data={'url': 'wrong://url'})
    assert response.status_code == 422

