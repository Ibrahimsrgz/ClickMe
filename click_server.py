from flask import Flask, redirect, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
        <body>
            <h2>Hoş geldiniz!</h2>
            <p><a href="/click">🔗 Tıklamak için buraya basın</a></p>
        </body>
    </html>
    '''

@app.route("/click")
def click():
    with open("clicks.txt", "a") as f:
        f.write(f"{request.remote_addr} - {time.ctime()}\n")
    return redirect("https://google.com", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
