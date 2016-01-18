
from flask import Flask
app = Flask(__name__,static_folder='../html/')

#importing this objects here creates a functional singleton pattern
from stage import stage
from dirmanager import dirmanager


