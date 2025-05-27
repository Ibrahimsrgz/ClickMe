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

@app.route("/", defaults={"number": None})
@app.route("/number", defaults={"number": None})
@app.route("/number=<int:number>")
def handle_request(number):
    return redirect("https://google.com", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)




