from flask import jsonify, request, redirect, abort

from start_ws import dirmanager, app

@app.route('/player/available/')
def available():
    return jsonify(dirmanager.list_available())


@app.route('/player/available.json')
def available_json():
    return jsonify(dirmanager.list_available_nested_dict()), 201


@app.route('/control/directory/', methods=["POST", "GET", "DELETE"])
def directory():
    if request.method == "POST":
        text = request.form['text']
        dirmanager.add_directory(sanitize(text))
        return  redirect("/")
    elif request.method == "DELETE":
        text = request.form['text']
        dirmanager.del_directory(sanitize(text))
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