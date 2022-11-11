import pyautogui as pg # pygui
import json


HOST = "0.0.0.0"
PORT = 5000
DEBUG  = False
VERBOSE = False
SECRET_KEY = "Change me to something random!"
MOUSE_SPEED = 10


def handle_keystroke(data):
    d = json.loads(data)

    modifiers = [
        "capslock",
        "shift",
        "ctrl",
        "fn",
        "win",
        "alt"
    ]
    for k, v in d.items():
        if v and k in modifiers:
            pg.keyDown(k)

    pg.press(d["key"])

    for k, v in d.items():
        if v and k in modifiers:
            pg.keyUp(k)


# def handle_mousemove(data):
#     d = json.loads(data)
#     pg.moveRel(d['x'], d['y'], duration=0.2)


def handle_mousemove(data):
    d = json.loads(data)
    if d['is_touch']:
        x, y = pg.position()
        x += d["x"] // MOUSE_SPEED
        y += d["y"] // MOUSE_SPEED
        pg.moveTo(x, y)
    else:
        pg.moveRel(d['x'], d['y'], duration=0.2)


def handle_mouseclick(data):
    d = json.loads(data)
    pg.click(button=d.get('key'))

def handle_text(data):
    d = json.loads(data)
    pg.typewrite(d['text'])
