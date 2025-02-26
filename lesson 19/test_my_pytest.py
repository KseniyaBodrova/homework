import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {"title": "fsak", "body": "baras", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('clear_post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def test_get_one_post(new_post_id):
    print('test get_one_posts')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id

@pytest.mark.smoke
def test_get_all_posts():
    print('test get_all_posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

def test_add_a_post():
    print('test add_a_post')
    body = {
    "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
    "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
    "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()['id'] == 101


