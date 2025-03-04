import time
from locust import HttpUser, task, between

class LocustTest(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def get(self):
        self.client.get("/get")

    @task(2)
    def post(self):
        self.client.post("/post", json=None)

    @task(4)
    def getLastTimestamp(self):
        self.client.get("/lasttimestamp")
