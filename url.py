import config
import os

def createurl(url, entry):
    open(os.path.join(config.url_location, entry), "w").writelines(url)
