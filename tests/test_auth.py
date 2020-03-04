import pytest
from flask import g, session
from flaskr.db import get_db

def test_register(client, app):
    assert client.get('/auth/register').status_code==200

    resposne = client.post(
        '/auth/register', data={'usenname':"a", 'password':"a"}
    )
    
    assert 'http://localhost/auth/login' == resposne.headers['Location']
    
    #Check DATABASE for registration
    with app.app_context():
        assert get_db().eecute(
            'select * from user where username="a"', 
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password','message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data = {'username':username, 'password':password}
    )
    assert message in response.data


def test_login(client, username, password):
    #Check for OK status_code resposne from route
    assert client.get('/auth/login').status_code == 200

    response = auth.login()
    assert response.header['Location'] == 'http://localhost/'

    with client:
        # Context variables "session" 
        # Sessions are like cookies storing data 
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password','message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
