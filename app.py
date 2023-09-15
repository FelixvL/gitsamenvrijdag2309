from flask import Flask
import jordy
import BartEnLukaApp
import Dirks_mooie_bestandje

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/jordy")
def hello_world2():
    return jordy.jordymethode()

@app.route("/team1")
def hello_world3():
    return BartEnLukaApp.bijnaweekend()


@app.route("/dirk")
def hello_world4():
    return Dirks_mooie_bestandje.mijnmethode()