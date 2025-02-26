import unittest
import requests


class PostApi(unittest.TestCase):



    def setUp(self):
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
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')


    @unittest.skip('getting post error')
    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)


class TestIndependent(unittest.TestCase):

    def test_get_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)


    def test_add_a_post(self):
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)