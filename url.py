import config
import os



def create(url, entry):
    """
    we write url to files so they are accessible through the uri
    """
    open(os.path.join(config.url_location, entry + ".url"), "w").writelines(url)