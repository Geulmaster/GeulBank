import requests

url = "http://localhost:5000/"

basic_user_info = {"username": "Eyal", "password": "chicaloca"}

def test_add():

    """
    Add 500 Jubot to Eyal
    """
    
    add_url = url + "add"
    add_credentials = basic_user_info
    add_credentials["amount"] = 500
    req = requests.post(url = add_url, json = add_credentials)
    assert req.json() == {'msg': '499 jubot added successfully to Eyal', 'status': 200}