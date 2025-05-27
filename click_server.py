#from flask import Flask, redirect, request
#import os
#import time
#app = Flask(__name__)

#@app.route("/")
#def home():

#    return redirect("https://google.com", code=302)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8000)

from flask import Flask, redirect, request
import time

app = Flask(__name__)

@app.route("/", defaults={"kullanici": None})
@app.route("/kullanici", defaults={"kullanici": None})
@app.route("/kullanici=<kullanici>")
def handle_request(kullanici):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdWu-G5nK4TKD-bR_x3BMZ8l2vwjbyJ71kUxFoZdaeCVw6bGw/viewform?usp=dialog", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)




