from flask import jsonify
from werkzeug.utils import redirect

from start_ws import app,  dir_manager, staged
from player import Player
current_player = Player()

@app.route('/player/pause')
def pause():
    current_player.pause()
    return redirect("/")


@app.route('/player/stop')
def stop():
    current_player.stop()
    return redirect("/")


@app.route('/player/play')
def play():
    global staged
    fullpath = [dir_manager.found_entry(x) for x in staged]
    current_player.start(fullpath)
    current_player.play()
    return redirect("/")


@app.route('/player/next')
def next_():
    current_player.next()
    return redirect("/")


@app.route('/player/prev')
def prev():
    return redirect("/")


@app.route('/player/current')
def current():
    return jsonify({"current": current_player.current()}), 201