import requests


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Все посты'


def one_post():
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response['id'] == post_id

def post_a_post():
    body = {
        'title': 'fgbhytgyjngjno',
        'body': 'bar',
        'userId': 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data=body, headers=headers)
    assert response.status_code == 201, 'Status code is incoreect'
    assert response.json()['id'] == 101, 'Id is incorrect'

def new_post():
    body = {
        'title': 'fgbhytgyjngjno',
        'body': 'bar',
        'userId': 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    return response.json()['id']

def clear(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def put_a_post():
    post_id = new_post()
    body = {
        "title": "new title",
        "body": "bar",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers).json()
    print(response)
    assert response['title'] == 'new title', 'Fail'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "title": "foo new",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers).json()
    assert response['title'] == 'foo new'
    clear(post_id)

def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    assert response.status_code == 200

# delete_a_post()
put_a_post()
# patch_a_post()

