from GeulBank.web.app import app
import unittest

basic_user_info = {"username": "Eyal", "password": "chicaloca"}

class Tests(unittest.TestCase):

    def test_register(self):
        """
        Register as a new client
        """
        register_credentials = basic_user_info.copy()
        register_credentials["username"] = "Eyalp"
        with app.test_client(self) as tester:
            req = tester.post('/register', json = register_credentials)
        self.assertEqual(req.get_json(), {'msg': 'Successfully signed up for the API', 'status': 200})

    def test_add(self):
        """
        Add 500 Jubot to Eyal
        """
        add_credentials = basic_user_info.copy()
        add_credentials["amount"] = 500
        with app.test_client(self) as tester:
            req = tester.post('/add', json = add_credentials)
        self.assertEqual(req.get_json(), {'msg': '499 jubot added successfully to Eyal', 'status': 200})

    def test_balance(self):
        """
        Test balance functionality
        """
        balance_credentials = basic_user_info.copy()
        with app.test_client(self) as tester:
            req = tester.post('/balance', json = balance_credentials)
        self.assertEqual(req.status_code, 200)
        return req.get_json()

    def test_transfer(self):
        """
        Test transfer functionality
        """
        transfer_credentials = basic_user_info.copy()
        transfer_credentials["to"] = "BANK"
        transfer_credentials["amount"] = 100
        amount_before = self.test_balance()["Own"]
        with app.test_client(self) as tester:
            req = tester.post('/transfer', json = transfer_credentials)
        amount_after = self.test_balance()["Own"]
        self.assertEqual(amount_before - amount_after, 100)
        self.assertEqual(req.status_code, 200)


if __name__=="__main__":
    unittest.main()