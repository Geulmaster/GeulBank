from locust import HttpUser, task, between
from GeulBank.tests.test_api import random_username

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def register(self):
        self.client.post("/register", json={"username":f"{random_username()}", "password":"bar"})


"""
locust -f load_test.py --host http://localhost:5000
"""