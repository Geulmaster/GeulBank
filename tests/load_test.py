from locust import HttpUser, task, between
from GeulBank.tests.test_api import random_username

basic_user_info = {"username": "Eyal", "password": "chicaloca"}

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def register(self):
        self.client.post("/register", json={"username":f"{random_username()}", "password":"bar"})

    
    @task
    def add(self):
        self.client.post("/add", json=basic_user_info)


    @task
    def balance(self):
        self.client.post("/balance", json=basic_user_info)


    @task
    def take_loan(self):
        self.client.post("/takeloan", json=basic_user_info)


    @task
    def pay_loan(self):
        self.client.post("/payloan", json=basic_user_info)

"""
locust -f load_test.py --host http://localhost:5000
"""
