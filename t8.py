import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():
    numbers = []

    p = 1

    while p <= 100:
        is_prime = True
        for i in range(2, p):
            if (p % i) == 0:
                is_prime = False
                break

        if is_prime:
            numbers.append(f"{p}")

        p += 1

    return "<br>".join(list(dict.fromkeys(numbers)))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
