from flask import Flask,jsonify,abort
from flask.ext.restful.representations.json import output_json

app = Flask(__name__)
current_player = None



@app.route('player/start/<entry>')
def start(entry):
    global  current_player
    current_player = MediaPlayer(entry)
    current_player.play()
    return 201

@app.route('player/pause')
def pause(entry):
    global  current_player
    current_player.pause()
    return 201

@app.route('player/stop')
def stop(entry):
    global  current_player
    current_player.stop()
    current_player = None
    return 201

@app.route('player/play')
def play(entry):
    global  current_player
    current_player.play()
    return 201

@app.route('config/directory',methods=["GET"])
def directories_put():
#FOR now, directories can't be set as a collection
    abort(403)

@app.route('config/directory',methods=["DELETE"])
def directories_delete():
#FOR now, directories can't be set as a collection
    abort(403)

@app.route('config/directory',methods=["GET"])
def directories_get():
    #TODO
    return 201

@app.route('config/directory/<entry>',methods=["PUT"])
def directory_put(entry):
    #TODO append directory on player dir list
    return 201

@app.route('config/directory/<entry>',methods=["GET"])
def directory_get(entry):
    #TODO list entry if in on player dir list
    return 201

@app.route('config/directory/<entry>',methods=["PUT"])
def directory_put(entry):
    return 201

if __name__ == '__main__':
    app.run()
