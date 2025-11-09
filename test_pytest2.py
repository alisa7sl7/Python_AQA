import pytest
import requests
import allure

@pytest.fixture
def num():
    return 3

@allure.feature('Posts')
@allure.story('Manipulate posts')
def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()

@allure.feature('Example')
@allure.story('Print')
def test_num(num):
    print(num)