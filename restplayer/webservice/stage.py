from flask import jsonify, request, redirect, abort
from nestedict import Nestedict
from werkzeug.utils import redirect
import playlist
from start import app,  sanitize, dir_manager, staged
import os
import config


@app.route('/stage/add/<entry>')
def stage_add(entry):
    if entry.rsplit(".", 1)[1] == "m3u":
        with open(os.path.join(config.playlist_location, entry)) as f:
            for music in f.readlines():
                staged.append(music)
        return redirect("/")
    if dir_manager.found_entry(sanitize(entry)) is not None:
        staged.append(entry)
    return redirect("/")


@app.route('/stage')
def stage():
    global staged
    return jsonify({"queue": staged})


@app.route('/stage/save/', methods=["POST", "GET"])
def stage_save():
    global staged
    if request.method == "POST":
        text = request.form['text']
        playlist.createplaylist(staged, text)
        return  redirect("/")
    elif request.method == "GET":
        return '''
    <!doctype html>
    <title>Save Playlist</title>
    <h1>Playlist Name</h1>
    <form action="/stage/save/" method=post>
      <p><input type=text name=text>
         <input type=submit value=Send>
    </form>
    '''
    else:
        print "UPS" \
              ""
        abort(400)


@app.route('/stage/clear/')
def stage_clear():
    global staged
    staged = []
    return redirect("/")


@app.route('/stage.json')
def stage_json():
    global staged
    ndict = Nestedict("Playing Queue", 1)
    for entry in staged:
        ndict.add_node("Playing Queue/" + unicode(entry), 1)
    return jsonify(dict(ndict))
