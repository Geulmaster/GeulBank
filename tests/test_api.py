from GeulBank.web.app import app
import unittest

url = "http://localhost:5000/"

basic_user_info = {"username": "Eyal", "password": "chicaloca"}

class Tests(unittest.TestCase):

    def test_add(self):
        """
        Add 500 Jubot to Eyal
        """
        add_url = url + "add"
        add_credentials = basic_user_info
        add_credentials["amount"] = 500
        with app.test_client(self) as tester:
            req = tester.post('/add', json = add_credentials)
        assert req.get_json() == {'msg': '499 jubot added successfully to Eyal', 'status': 200}

if __name__=="__main__":
    unittest.main()