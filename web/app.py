from flask import Flask
from flask_restful import Api, Resource

from GeulBank.web.helpers import wrapper
from GeulBank.web.actions import resources

app = Flask(__name__)
api = Api(app)

api.add_resource(resources.Register, '/register')
api.add_resource(resources.Add, '/add')
api.add_resource(resources.Transfer, '/transfer')
api.add_resource(resources.Balance, '/balance')
api.add_resource(resources.TakeLoan, '/takeloan')
api.add_resource(resources.PayLoan, '/payloan')
api.add_resource(resources.Leave, '/leave')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)