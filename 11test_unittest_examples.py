import unittest
import requests
import sys


class TestPostApi(unittest.TestCase):
    def setUp(self):
        body = {
            "userId": 2,
            "title": "ea molestias quasi exeepellat qui ipsa sit aut",
            "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
        }

        headers = {'content-type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts',
                                 json=body,
                                 headers=headers
                                 )
        self.post_id = response.json()['id']
        print(f'Post created with id: {self.post_id}')

    def tearDown(self) -> None:
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted with id: {self.post_id}')

    @unittest.skip('Bug - #1')
    def test_get_one_post(self):
        print('test')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)

class TestIndependent(unittest.TestCase):

    @unittest.skipIf(sys.platform == 'win 32', 'not for Windows test')
    def test_get_all_posts(self):
        print('test')
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)
        # assert len(response) == 101, 'Not all posts returned'

    def test_add_post(self):
        print('test')
        body = {
            "userId": 1,
            "title": "ea molestias quasi exeepellat qui ipsa sit aut",
            "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
        }

        headers = {'content-type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts',
                                 json=body,
                                 headers=headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'],101 )

'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''