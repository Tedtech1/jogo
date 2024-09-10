from flask import Flask, render_template, request

app = Flask(__name__)

# Número secreto
numero_secreto = 6  # Altere o número secreto se desejar

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    coracoes = 0
    if request.method == "POST":
        try:
            palpite = int(request.form["palpite"])
            if palpite < numero_secreto:
                mensagem = "Muito baixo! Tente novamente."
            elif palpite > numero_secreto:
                mensagem = "Muito alto! Tente novamente."
            else:
                mensagem = "Parabéns! Você é o amor da minha vida!"
                coracoes = 5  # Número de corações a exibir quando acertar
        except ValueError:
            mensagem = "Por favor, insira um número válido."
    return render_template("index.html", mensagem=mensagem, coracoes=coracoes)

if __name__ == "__main__":
    app.run(debug=True)
