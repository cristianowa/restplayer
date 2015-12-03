from flask import Flask,jsonify,abort
from flask.ext.restful.representations.json import output_json
from player import Player, NOTFOUND
app = Flask(__name__)
current_player = Player()



@app.route('player/start/<entry>')
def start(entry):
    current_player.start(entry)
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
    return str(current_player.get_directory()), 201

@app.route('config/directory/<entry>',methods=["PUT"])
def directory_put(entry):
    current_player.add_directory(entry)
    return 201

@app.route('config/directory/<entry>',methods=["GET"])
def directory_get(entry):
    output = current_player.get_directory(entry)
    if output == NOTFOUND:
        return NOTFOUND, 404
    return output, 201

@app.route('config/directory/<entry>',methods=["DELETE"])
def directory_delete(entry):
    current_player.del_directory(entry)
    return 201

if __name__ == '__main__':
    app.run()
