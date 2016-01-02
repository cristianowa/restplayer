#!/usr/bin/python
import os

from flask import Flask, jsonify, abort, request, redirect
from werkzeug import secure_filename
from nestedict import Nestedict
import alsaaudio

from player import Player, NOTFOUND
import config
import url
app = Flask(__name__,static_folder='html/')

current_player = Player()
staged = []

def sanitize(s):
    return unicode(s)

@app.route('/stage/add/<entry>')
def stage_add(entry):
    global staged
    global current_player
    if current_player.found_entry(sanitize(entry)) is not None:
        staged.append(entry)
    return redirect("/")

@app.route('/stage')
def stage():
    global staged
    return jsonify({"queue":staged})

@app.route('/stage/save/')
def stage_save():
    global staged
    return redirect("/")

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
    global staged
    global  current_player
    current_player.start(staged)
    current_player.play()
    return redirect("/")

@app.route('/player/next')
def next_():
    global  current_player
    current_player.next()
    return redirect("/")

@app.route('/player/prev')
def prev():
    global  current_player
    return redirect("/")

@app.route('/player/current')
def current():
    global current_player
    return jsonify({"current":current_player.current()}),201

@app.route('/player/available/')
def available():
    global current_player
    return jsonify(current_player.list_available())


@app.route('/player/available.json')
def available_json():
    global current_player
    return jsonify(current_player.list_available_nested_dict()), 201

@app.route('/control/directory/', methods=["POST","GET","DELETE"])
def directory():
    global current_player
    if request.method == "POST":
        text = request.form['text']
        current_player.add_directory(sanitize(text))
        return  redirect("/")
    elif request.method == "DELETE":
        text = request.form['text']
        current_player.del_directory(sanitize(text))
        return  redirect("/")
    elif request.method == "GET":
        return '''
    <!doctype html>
    <title>Add New Directory</title>
    <h1>Add New Directory</h1>
    <form action="/control/directory/" method=post>
      <p><input type=text name=text>
         <input type=submit value=Send>
    </form>
    '''
    else:
        print "UPS" \
              ""
        abort(400)



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


@app.route('/upload/playlist/', methods=["POST","GET"])
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

@app.route('/upload/music/', methods=["POST","GET"])
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

@app.route("/volume/up")
def volume_up():
    m = alsaaudio.Mixer()
    m.setmute(0)
    vol = m.getvolume()[0]
    if vol+5 > 100:
        vol = 95
    m.setvolume(vol+5)
    return redirect("/")

@app.route("/volume/down")
def volume_down():
    m = alsaaudio.Mixer()
    vol = m.getvolume()[0]
    if vol-5 < 0:
        vol = 5
    m.setvolume(vol-5)
    return redirect("/")

@app.route("/volume/off")
def volume_off():
    m = alsaaudio.Mixer()
    m.setmute(1)
    return redirect("/")

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
    app.run(debug=True, host='0.0.0.0')

