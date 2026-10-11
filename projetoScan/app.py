import socket
from flask import Flask, render_template, request

app = Flask(__name__)

ports = [
    20,
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    389,
    443,
    587,
    3306,
    3389,
    5432,
    8080,
    8443,
]


@app.route("/", methods=["GET", "POST"])
def home():
    portas_abertas = []
    ip_digitado = ""

    if request.method == "POST":
        ip_digitado = request.form.get("entrada_Ip")

        if ip_digitado:
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                code = client.connect_ex((ip_digitado, port))

                if code == 0:
                    portas_abertas.append(port)
                    print(f"[+] Porta {port} aberta")
                client.close()

    return render_template("index.html", ip=ip_digitado, portas=portas_abertas)


if __name__ == "__main__":
    app.run(debug=True)