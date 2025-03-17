from flask import Flask
import random

app = Flask(__name__)

funlist=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
"El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"]

@app.route("/")
def hello_world():
    return """<h1>Hello, World!</h1>'
    <a href="/datos">¡Ver un dato aleatorio!</a>
    <a href="/ROUTE">       Lanzar Moneda Digital.</a>
"""
@app.route("/datos")
def fun_facts():
    return f'<p>{random.choice(funlist)}</p>'
@app.route("/ROUTE")
def LEROUTE():
    DigCoin=random.randint(1,2)
    if DigCoin==1:
        return """Lanzando Moneda Digital... 
        <a> Cruz. </a> 
        <a href="/ROUTE">       Tirar otra vez? click aqui.</a>"""
    else:
        return """Lanzando Moneda Digital... 
        <a> Cara. </a>
        <a href="/ROUTE">       Tirar otra vez? Click aqui.</a>"""

app.run(debug=True)
