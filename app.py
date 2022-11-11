import external
from flask import *
from flask_socketio import *


app = Flask(__name__)
app.config['SECRET_KEY'] = external.SECRET_KEY
socketio = SocketIO(app)


@app.route("/")
def index():
    return """
<a href="keyboard">keyboard</a>
<a href="mouse">mouse</a>
<a href="text">text</a>
"""

# --------------------------------- keyboard ---------------------------------
@app.route("/keyboard/")
def keyboard():
    return render_template("keyboard.html")


@socketio.on('keystroke')
def keystroke(data):
    if external.VERBOSE:
        print("-"*36)
        print(data)
        print("-"*36)
    external.handle_keystroke(data)


@app.route("/text/")
def text():
    return render_template("text.html")


@socketio.on('keystroke')
def handle_text(data):
    if external.VERBOSE:
        print("-"*36)
        print(repr(data))
        print("-"*36)
    external.handle_text(data)


# --------------------------------- mouse ---------------------------------
@app.route("/mouse/")
def mouse():
    return render_template("mouse.html")


@socketio.on('mousemove')
def keystroke(data):
    if external.VERBOSE:
        print("-"*36)
        print(data)
        print("-"*36)
    external.handle_mousemove(data)


@socketio.on('mouseclick')
def keystroke(data):
    if external.VERBOSE:
        print("-"*36)
        print(data)
        print("-"*36)
    external.handle_mouseclick(data)


if __name__ == '__main__':
    if external.VERBOSE:
        print("pc-remote started.")
    socketio.run(app,
                 host=external.HOST,
                 port=external.PORT,
                 debug=external.DEBUG)
