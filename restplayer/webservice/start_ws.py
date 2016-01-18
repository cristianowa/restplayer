from dirmanager import dirmanager
from flask import Flask
from stage import stage
app = Flask(__name__,static_folder='../html/')

dir_manager = dirmanager


