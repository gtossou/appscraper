"""
This file (test_stocks.py) contains the functional tests for the app.py file.
"""
from ...web.routes import app


def test_add_prospect_app_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/add_prospect_app')
        assert response.status_code == 200
        assert b'Nom' in response.data
        assert b'Votre mail' in response.data
        assert b"Nom de l'application" in response.data
        assert b"Url de l'application" in response.data


def test_add_prospect_app_post():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """

    with app.test_client() as client:
        response = client.post('/add_prospect_app',
                               data={'user_name': 'KT',
                                     'user_mail': 'test@gmail.com',
                                     'app_name': 'fakeapp',
                                     'app_url': 'com.fakeapp'},
                               follow_redirects=True)
        assert response.status_code == 200
        assert b'Nom' in response.data
        assert b'Mail' in response.data
        assert b"Nom de l'application" in response.data
        assert b"Url de l'application" in response.data
        assert b'KT' in response.data
        assert b'test@gmail.com' in response.data
        assert b'fakeapp' in response.data
        assert b'com.fakeapp' in response.data
