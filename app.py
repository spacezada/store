from flask import Flask
import os

app = Flask(__name__, static_folder=os.path.abspath("view/static"),template_folder=os.path.abspath("view/templates" ))

from controller import home_controller
from controller import produto_controller
from controller import store_controller