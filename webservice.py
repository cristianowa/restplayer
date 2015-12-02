from flask import Flask
from vlc import  MediaPlayer

app = Flask(__name__)
current_player = None

@app.route('/start/<entry>')
def start(entry):
    global  current_player
    current_player = MediaPlayer(entry)
    current_player.play()

@app.route('/pause')
def pause(entry):
    global  current_player
    current_player.pause()

@app.route('/stop')
def stop(entry):
    global  current_player
    current_player.stop()
    current_player = None

@app.route('/play')
def play(entry):
    current_player.play()


if __name__ == '__main__':
    app.run()
