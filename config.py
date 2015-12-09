
home_dir = None
url_location = ".restplayer/url"
playlist_location = ".restplayer/playlists"
uploaded_location = ".restplayer/uploaded"


import os
if home_dir is None:
    home_dir = os.environ["HOME"]
url_location = os.path.join(home_dir, url_location)
playlist_location = os.path.join(home_dir, playlist_location)
uploaded_location = os.path.join(home_dir, uploaded_location)

import shutil
def __setup__():
    try:
        os.makedirs(url_location)
    except:
        pass
    try:
        os.makedirs(playlist_location)
    except:
        pass
    try:
        os.makedirs(uploaded_location)
    except:
        pass


__setup__()