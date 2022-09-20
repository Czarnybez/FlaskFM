from flask.views import MethodView
from wtforms import Form
from flask import Flask

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return "Hello"


class BillFormPage(MethodView):
    pass

class ResultsPage(MethodView):
    pass

class BillForm(Form):
    pass

