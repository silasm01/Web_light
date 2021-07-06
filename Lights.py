from flask import Flask, redirect, url_for, render_template, request
import yeelight
from yeelight import discover_bulbs
from yeelight import Bulb
import time

bulbg = Bulb("192.168.8.108")
strip = Bulb("192.168.8.199")
device = ""

app = Flask(__name__)

def light(device1):
        c = 0
        count = 0
        g = ""
        with open('devices.txt','r') as f:
                for line in f:
                        c += 1
                        if line == device1 + "\n":
                                c += 1
                                count = c
                import linecache
                bulb = Bulb(linecache.getline('devices.txt', count).strip())
                print(bulb)
        bulb.toggle()

@app.route("/")
def start():
        return "<p>Hello, World!</p>"

@app.route("/<device>/toggle")
def toggle(device):
        return "<p>Hello, World!</p>", light(device)

@app.route("/light_1/brightness/<brightness>")
def light1_brightness(brightness):
        return bulb.set_brightness(int(brightness))

if __name__ == "__main__":
    app.run(debug=True, port=80)
