from flask import Flask
app= Flask(__name__)

#Ruta simple
@app.route('/')
def home():
    return 'Hola Mundo FLASK'

#Ruta con parámetros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola, '+nombre+'!!!'

#Ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado, Error de capa 8 !!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el método del enío de tu ruta (GET o POST !!!)',405

#Ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'soy el mismo recurso del servidor'

#Ruta POST
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'soy un formulario :D'

if __name__ == '__main__':
    app.run(port=3000,debug=True)