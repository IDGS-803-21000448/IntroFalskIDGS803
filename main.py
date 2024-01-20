from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    #return "<h1>Hola <br> Mundo</h1>"
    escuela = "UTL!!!"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html",escuela = escuela, alumnos = alumnos)

@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde HOLA!!!!! <h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1> Hola "+name+"</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return f"ID: {id} Nombre: {name}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es {n1} + {n2} = {n1+n2}"

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab = "UTL"):
    return "El Valor es "+ab

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")



if __name__ == "__main__":
    app.run(debug=True)
