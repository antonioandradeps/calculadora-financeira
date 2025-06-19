# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # --- Seu código Python aqui ---
    fat = 5000
    des = 1300
    luc = fat - des
    pre = 0

    if luc < 0:
        pre = des - fat
        luc = 0
    else:
        pre = 0
    # --- Fim do seu código Python ---

    resultados = {
        'faturamento': fat,
        'despesa': des,
        'lucro': luc,
        'prejuizo': pre
    }

    return render_template('resultado.html', dados=resultados)

# O bloco if __name__ == '__main__': app.run(debug=True)
# NÃO é necessário no PythonAnywhere porque eles têm o próprio servidor WSGI.