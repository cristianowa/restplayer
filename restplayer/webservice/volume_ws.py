import alsaaudio

from werkzeug.utils import redirect

from start_ws import app


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