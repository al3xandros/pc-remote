from flask import *
import pyautogui as pg
import os


HOST = "0.0.0.0"
PORT = 5000

app = Flask(__name__)
step = 10

def move_mouse(k, setp=10):
    if k == 'KeyS':
        pg.moveRel(xOffset=0, yOffset=setp)
    elif k == 'KeyW':
        pg.moveRel(xOffset=0, yOffset=-setp)
    elif k == 'KeyA':
        pg.moveRel(xOffset=-setp, yOffset=0)
    elif k == 'KeyD':
        pg.moveRel(xOffset=setp, yOffset=0)
    elif k == 'Click':
        pg.click()
    elif k == 'Click2':
        pg.click(button=pg.SECONDARY)
    elif k == "Enter1":
        pg.press(pg.KEYBOARD_KEYS[98])
    elif k == "BackSpace":
        pg.press(pg.KEYBOARD_KEYS[78])


def step_handle(v):
    global step
    if v == "+":
        step += 5
    elif v == "-":
        step -= 5

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method.upper() == "POST":
        data = request.data.decode("utf-8").split(";")
        if data[0] == "k":
            move_mouse(data[1], setp=step)
        elif data[0] == "s":
            step_handle(data[1])
        elif data[0] == "t":
            pg.typewrite(data[1])
    return render_template("index.html", step=step)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
