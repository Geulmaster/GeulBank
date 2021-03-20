from GeulBank.web.app import app
from GeulBank.web.helpers import wrapper
import unittest
import string
from random import *

def random_username():
    characters = string.ascii_letters \
        + string.punctuation \
        + string.digits
    username = "".join(choice(characters)
        for x in range(randint(6, 10)))
    return username

basic_user_info = {"username": "Eyal", "password": "chicaloca"}
bank_info = {"username": "BANK", "password": "chicaloca"}

class Tests(unittest.TestCase):


    def test_register(self, info = basic_user_info):
        """
        Register as a new client
        """
        register_credentials = info.copy()
        username = random_username()
        register_credentials["username"] = username
        with app.test_client(self) as tester:
            req = tester.post('/register', json = register_credentials)
        print(f"signed up as {username}")
        self.assertEqual(req.get_json(), {'msg': 'Successfully signed up for the API', 'status': 200})
        return username


    def test_add(self, info = basic_user_info):
        """
        Add 500 Jubot to Eyal
        """
        add_credentials = info.copy()
        add_credentials["amount"] = 500
        with app.test_client(self) as tester:
            req = tester.post('/add', json = add_credentials)
        self.assertEqual(req.get_json(), {'msg': '499 jubot added successfully to Eyal', 'status': 200})


    def test_balance(self, info = basic_user_info):
        """
        Test balance functionality
        """
        balance_credentials = info.copy()
        with app.test_client(self) as tester:
            req = tester.post('/balance', json = balance_credentials)
        self.assertEqual(req.status_code, 200)
        return req.get_json()


    def test_transfer(self, info = basic_user_info):
        """
        Test transfer functionality
        """
        transfer_credentials = info.copy()
        transfer_credentials["to"] = "BANK"
        transfer_credentials["amount"] = 100
        amount_before = self.test_balance()["Own"]
        with app.test_client(self) as tester:
            req = tester.post('/transfer', json = transfer_credentials)
        amount_after = self.test_balance()["Own"]
        self.assertEqual(amount_before - amount_after, 100)
        self.assertEqual(req.status_code, 200)


    def test_takeLoan(self, info = basic_user_info):
        """
        Test loan getting
        """
        transfer_credentials = info.copy()
        transfer_credentials["amount"] = 100
        amount_before = self.test_balance()["Own"]
        with app.test_client(self) as tester:
            req = tester.post('/takeloan', json = transfer_credentials)
        amount_after = self.test_balance()["Own"]
        self.assertEqual(amount_after - amount_before, 100)
        self.assertEqual(req.status_code, 200)


    def test_payLoan(self, info = basic_user_info):
        """
        Test loan payment
        """
        transfer_credentials = info.copy()
        transfer_credentials["amount"] = 100
        user_debt_before = self.test_balance()["Debt"]
        with app.test_client(self) as tester:
            req = tester.post('/payloan', json = transfer_credentials)
        user_debt_after = self.test_balance()["Debt"]
        self.assertEqual(req.status_code, 200)
        self.assertEqual(user_debt_before - user_debt_after, int(transfer_credentials["amount"]))


    def test_leaving(self, info = basic_user_info):
        """
        Test unregistration from the API
        """
        transfer_credentials = info.copy()
        with app.test_client(self) as tester:
            req = tester.post('/leave', json = transfer_credentials)
        self.assertEqual(req.status_code, 200)
        assert not wrapper.user_exists(transfer_credentials["username"])


if __name__=="__main__":
    unittest.main()
    