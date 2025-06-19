# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Esta rota exibe o formulário para o usuário digitar os valores.
    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    # Esta rota processa os dados enviados pelo formulário.
    if request.method == 'POST':
        try:
            # Pega os valores do formulário (que virão como strings)
            fat_str = request.form['faturamento']
            des_str = request.form['despesas']

            # Converte para números inteiros
            fat = int(fat_str)
            des = int(des_str)

            # --- Seu código de cálculo Python aqui ---
            luc = fat - des
            pre = 0 # Inicializa prejuízo

            if luc < 0:
                pre = des - fat
                luc = 0
            else:
                pre = 0
            # --- Fim do seu código de cálculo Python ---

            # Agrupa os resultados em um dicionário
            resultados = {
                'faturamento': fat,
                'despesa': des,
                'lucro': luc,
                'prejuizo': pre
            }

            # Renderiza o template de resultado com os dados
            return render_template('resultado.html', dados=resultados)

        except ValueError:
            # Caso o usuário digite algo que não seja um número
            erro_msg = "Por favor, digite apenas números válidos para faturamento e despesas."
            return render_template('formulario.html', erro=erro_msg)
        except Exception as e:
            # Captura outros erros inesperados
            erro_msg = f"Ocorreu um erro inesperado: {e}"
            return render_template('formulario.html', erro=erro_msg)
    else:
        # Se alguém tentar acessar /calcular diretamente sem POST, redireciona para o formulário.
        return redirect(url_for('index'))

# Não precisamos do app.run() para o PythonAnywhere/Render.
