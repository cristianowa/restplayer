from flask import jsonify, request, redirect, abort
from nestedict import Nestedict
from werkzeug.utils import redirect
from start_ws import app, dirmanager, stage


@app.route('/stage/add/<entry>')
def stage_add(entry):
    stage.add(entry)
    return redirect("/")

@app.route('/stage/adddir/<entry>')
def stage_adddir(entry):
    stage.adddir(entry.replace("_","/"))
    return redirect("/")


@app.route('/stage')
def showstage():
    return jsonify({"queue": stage.array})


@app.route('/stage/save/', methods=["POST", "GET"])
def stage_save():
    if request.method == "POST":
        text = request.form['text']
        stage.createplaylist(text)
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
    stage.clear()
    return redirect("/")


@app.route('/stage.json')
def stage_json():
    ndict = Nestedict("Playing Queue", 1)
    for entry in stage.array:
        ndict.add_node("Playing Queue/" + unicode(entry), 1)
    return jsonify(dict(ndict))
