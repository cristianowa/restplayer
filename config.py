
home_dir = None
base_dir = None
url_location = "url"
playlist_location = "playlists"
uploaded_location = "uploaded"
player_persistance = "persistance.shelve"

import os
if home_dir is None:
    home_dir = os.environ["HOME"]
if base_dir is None:
    base_dir = os.path.join(home_dir, ".restplayer")
url_location = os.path.join(base_dir, url_location)
playlist_location = os.path.join(base_dir, playlist_location)
uploaded_location = os.path.join(base_dir, uploaded_location)
player_persistance = os.path.join(base_dir, player_persistance)
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