from flask import Flask, render_template

app = Flask(__name__)  

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/doctrina")
def doctrina():
    return render_template("doctrina.html")

@app.route("/sermones")
def sermones():
    return render_template("sermones.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)