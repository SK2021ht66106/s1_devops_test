from application import app


def test_hello():
    response = app.test_client().get('/')
    print('*** Response from unit test: {}'.format(response))

    assert response.status_code == 200
    assert response.data == b'Github Actions demo!'

def test():
    pass
