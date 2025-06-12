from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa (SUT)
    - A: Assert - Garanta que A e A
    """
    # Arrange
    # client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_hello_deve_retornar_ok_e_ola_mundo_em_html(client):
    response = client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>olá mundo</h1>' in response.text
