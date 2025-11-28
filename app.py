from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "senha-secreta"  

cadastro = {
    "Sofia": {
        "email": "sofia@gmail.com",
        "senha": "senha123",
        "perfil": "Aluno",
        "descricao": "Aluna muito dedicada com boas notas",
        "genero": "Feminino",
        "prontuario": "SP314965X",
        "disciplina": "Matemática",
        "orientador": "Maria"
    },

    "Julia": {
        "email": "julia.estudante@gmail.com",
        "senha": "haydenchrislover",
        "perfil": "Aluno",
        "descricao": "Aluna em conselho estudantil",
        "genero": "Feminino",
        "prontuario": "SP213465Y",
        "disciplina": "Fisica",
        "orientador": "Lucas"
    },

    "Lucas": {
        "email": "lucas.professor@gmail.com",
        "senha": "proflucas",
        "perfil": "Professor",
        "descricao": "Docente: mestre em biologia e fisica",
        "genero": "Masculino",
        "prontuario": "SP987655Z",
        "disciplina": "Fisica",
        "orientador": "-"
    }
}


@app.route("/")
def inicio():
    if "usuario" in session:
        return redirect(url_for("painel"))
    return redirect(url_for("entrar"))


@app.route("/entrar", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if nome in cadastro and cadastro[nome]["senha"] == senha and cadastro[nome]["email"] == email:
            session["usuario"] = nome
            return redirect(url_for("painel"))
        else:
            return render_template("login.html", erro="Dados incorretos, tente novamente.")

    return render_template("login.html")


@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect(url_for("entrar"))
    
    usuario = session["usuario"]
    dados = cadastro[usuario] 

    return render_template("informacoes.html", usuario=usuario, dados=dados)


@app.route("/sair")
def sair():
    session.pop("usuario")
    return redirect(url_for("entrar"))


if __name__ == "__main__":
    app.run(debug=True)