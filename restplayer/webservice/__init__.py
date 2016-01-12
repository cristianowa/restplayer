#!/usr/bin/python
import os

import config
from flask import request, redirect

from start import app, dir_manager, sanitize

import  player_ws, stage, dirmanager_ws, volume

@app.route('/upload/playlist/', methods=["POST", "GET"])
def uploadplaylist():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit(".", 1)[1] is "m3u":
            filename = sanitize(file.filename)
            file.save(os.path.join(config.playlist_location, filename))
            return redirect("/")
    return '''
    <!doctype html>
    <title>Upload new Playlist</title>
    <h1>Upload new Playlist</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    ''', 201

@app.route('/upload/music/', methods=["POST", "GET"])
def uploadmusic():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit(".", 1)[1] in config.supported_extensions:
            filename = sanitize(file.filename)
            file.save(os.path.join(config.uploaded_location, filename))
            return redirect("/")
    return '''
    <!doctype html>
    <title>Upload new Music</title>
    <h1>Upload new Music File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    ''', 201


@app.route("/map/", methods=['POST', 'GET'])
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        links.append(str(rule.rule).replace("<", "[").replace(">", "]"))
    return str(links), 201

@app.route('/')
def root():
    return app.send_static_file('player.html')

@app.route('/<filename>')
def getfile(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

