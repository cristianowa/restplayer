#!/usr/bin/python
import os
from flask import Flask, jsonify, abort, request, send_from_directory, redirect
from flask.ext.restful.representations.json import output_json
from werkzeug import secure_filename

from player import Player, NOTFOUND
import config
import url
app = Flask(__name__,static_folder='html/')
current_player = Player()



@app.route('/player/start/<entry>')
def start(entry):
    current_player.start(entry)
    return redirect("/")

@app.route('/player/pause')
def pause():
    global  current_player
    current_player.pause()
    return redirect("/")

@app.route('/player/stop')
def stop():
    global  current_player
    current_player.stop()
    return redirect("/")

@app.route('/player/play')
def play():
    global  current_player
    current_player.play()
    return redirect("/")

@app.route('/player/next')
def next():
    global  current_player
    current_player.next()
    return redirect("/")

@app.route('/player/prev')
def prev():
    global  current_player
    return redirect("/")

@app.route('/player/available')
def available():
    global current_player
    return str(current_player.list_available()), 201

@app.route('/control/directory',methods=["PUT"])
def directories_put():
#FOR now, directories can't be set as a collection
    abort(403)

@app.route('/control/directory',methods=["DELETE"])
def directories_delete():
#FOR now, directories can't be set as a collection
    abort(403)

@app.route('/control/directory',methods=["GET"])
def directories_get():
    return str(current_player.get_directory()), 201

@app.route('/control/directory/<entry>',methods=["PUT"])
def directory_put(entry):
    current_player.add_directory(entry)
    return redirect("/")

@app.route('/control/directory/<entry>',methods=["GET"])
def directory_get(entry):
    output = current_player.get_directory(entry)
    if output == NOTFOUND:
        return NOTFOUND, 404
    return redirect("/")

@app.route('/control/createurl/', methods=["POST", "GET"])
@app.route('/control/createurl/<entry>', methods=["POST", "GET"])
def createurl(entry=None):
    if request.method == "POST":
        if entry == None:
            entry = request.form["entry"]
        url.create(request.form['url'], entry)
        return redirect("/")
    return '''
    <!doctype html>
    <title>Createurl</title>
    <h1>Create new url</h1>
    <form action="." method=post>
      <h4>Url:</h4>
      <p><input type=text name=url>
      <h4>Entry:</h4>
      <p><input type=text name=entry>
         <input type=submit value=Create>
    </form>
    ''', 201


@app.route('/config/directory/<entry>',methods=["DELETE"])
def directory_delete(entry):
    current_player.del_directory(entry)
    return 201

@app.route('/upload/playlist/', methods=["POST","GET"])
def uploadplaylist():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit(".", 1)[1] is "m3u":
            filename = secure_filename(file.filename)
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

@app.route('/upload/music/', methods=["POST","GET"])
def uploadmusic():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit(".", 1)[1] is "m3u":
            filename = secure_filename(file.filename)
            file.save(os.path.join(config.uploaded_location, filename))
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


@app.route("/map/", methods=['POST','GET'])
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
    app.run(debug=True)

