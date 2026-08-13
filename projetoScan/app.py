from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanport", methods=["POST"])
def scanport():
    host = request.form.get("entrada_Ip")
    port = []

if __name__ == "__main__":
    app.run(debug=True)

"""

import socket

host = None
ports = None

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((host, port))
    if code == 0:
        print("[+] {} open".format(port))
"""
