import pytest
import requests
import allure

@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('bye')


@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.smoke
def test_get_one_post(new_post_id, hello):
    print('test')
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check that post id is {new_post_id}'):
      assert response == {11}

@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение всех постов')
@pytest.mark.smoke
def test_get_all_posts():
    print('test')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Posts')
@allure.story('Manipulate posts')
@pytest.mark.regression
def test_add_post():
    print('test')
    with allure.step('Prepare test data'):
        body = {
        "userId": 1,
        "title": "ea molestias quasi exeepellat qui ipsa sit aut",
        "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    }

    headers = {'content-type': 'application/json'}

    with allure.step('Run request to create a post'):
        response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             json=body,
                             headers=headers)

    with allure.step('Check response code is 201'):
      assert response.status_code == 201
    with allure.step('Check id of created post is 101'):
     assert response.json()['id'] ==101

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.regression
def test_one():
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.parametrize('logins', ['', ' ', 'fhbfbf  '])
def test_two(logins):
    print('test')
    assert 1 == 1


@allure.feature('Example')
@allure.story('Equals')
def test_three():
    assert 1 == 1