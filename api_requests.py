from http.client import responses

import requests
#import json

def all_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    assert len(response) == 101 , 'Not all posts returned'



def one_post():
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id


def post_a_post():
    # body = json.dumps({
    #     "userId": 1,
    #     "title": "ea molestias quasi exeepellat qui ipsa sit aut",
    #     "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    # })


    body ={
            "userId": 1,
            "title": "ea molestias quasi exeepellat qui ipsa sit aut",
            "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    }

    headers = {'content-type': 'application/json'}
    response= requests.post('https://jsonplaceholder.typicode.com/posts', json= body, headers= headers)
    assert response.status_code == 201, 'Status code should be 201'
    assert response.json()['id'] == 101, 'Id is incorrect'

def new_post():
    body ={
            "userId": 2,
            "title": "ea molestias quasi exeepellat qui ipsa sit aut",
            "body": "et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    }

    headers = {'content-type': 'application/json'}
    response= requests.post('https://jsonplaceholder.typicode.com/posts', json= body, headers= headers)
    return response.json()['id']

def clear(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def put_a_post():
    post_id = new_post()
    body = {
        "userId": 1,
        "title": "UPD ea molestias quasi exeepellat qui ipsa sit aut",
        "body": "UPD et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    }

    headers = {'content-type': 'application/json'}
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers).json()
    assert response['title'] == 'UPD ea molestias quasi exeepellat qui ipsa sit aut'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "userId": 8,
        "body": "UPD et iusto sedtateptatem doloribus  eius odio et labore et velit aut"
    }

    headers = {'content-type': 'application/json'}
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers).json()
    clear(post_id)

def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


