from http import HTTPStatus

from fastapi_zero.security import create_access_token


def test_get_token(client, user):
    response = client.post(
        '/auth/token/',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_get_current_user_not_found__exercicio(client):
    data = {'no-email': 'test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_does_not_exists__exercicio(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_user_invalid(client, user):
    response = client.post(
        '/auth/token/',
        data={'username': 'test', 'password': 'test'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_email_invalid(client, user):
    response = client.post(
        '/auth/token/',
        data={'username': user.email, 'password': 'test'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}
