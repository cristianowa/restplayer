from flask import Flask

from dirmanager import DirManager

app = Flask(__name__,static_folder='../html/')

dir_manager = DirManager()
staged = []


def sanitize(s):
    return unicode(s)