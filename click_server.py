from flask import Flask, redirect, request
import os
import time

app = Flask(__name__)

LOG_PATH = "/tmp/clicks.txt"

# Dosya varsa dokunma, yoksa oluştur
if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, "w") as f:
        f.write("Click Logs\n")

@app.route("/")
def home():
    log_line = f"{request.remote_addr} - {time.ctime()}\n"
    with open(LOG_PATH, "a") as f:
        f.write(log_line)
    print(log_line.strip())  # Render log ekranında görelim
    return redirect("https://google.com", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
