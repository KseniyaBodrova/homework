from locust import task, HttpUser

class Resources(HttpUser):

    def on_start(self) -> None:
        response = self.client.post('/posts')

    @task
    def get_all_resources(self):
        self.client.get('/posts')