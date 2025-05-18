from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (SUT)
    - A: Assert - Garanta que A e A
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_deve_retornar_ok_e_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK
    assert response.text == """
    <html>
        <head>
            <title>Exercício Aula 02</title>
        </head>
        <body>
            <h1>olá mundo</h1>
        </body>
    </html>
    """
