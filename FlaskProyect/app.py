from flask import Flask, jsonify, render_template, request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb #Importación del MySQL

app= Flask(__name__)

#Definir las variables
app.config['MYSQL_HOST']="localhost" #toma el 27001
app.config['MYSQL_USER']="root" #Definir el usuario
app.config['MYSQL_PASSWORD']="Cynthia13" #Definir la pw
app.config['MYSQL_DB']="DBflask"
app.secret_key= 'mysecretkey'
#app.config['MYSQL_PORT']="3306" //usar solo en cambio de puerto

#Declarar una variable de mysql pasando la estancia de MySQL de mi propia app
mysql= MySQL(app)



#Ruta simple / de inicio
@app.route('/')
def home():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM BD_Albums WHERE State = 1')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, albums= consultaTodo)
    
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums= [])
    
    finally:
        cursor.close()
        
#Ruta para actualizar formulario
@app.route('/formUpdate/<int:id>')
def formUpdate(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM BD_Albums WHERE id_Album = %s', (id,))
        album = cursor.fetchone()
        if album:
            return render_template('formUpdate.html', album=album)
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error: {e}')
        return redirect(url_for('home'))
    finally:
        cursor.close()
        
#Ruta para procesar la actualización
@app.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizarAlbum(id):
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    if not Vtitulo or not Vartista or not Vanio:
        flash('Todos los campos son obligatorios')
        return redirect(url_for('formUpdate', id=id))

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE BD_Albums SET album=%s, artista=%s, anio=%s WHERE id_Album=%s', (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        flash('Album Actualizado en BD')
        return redirect(url_for('home'))
    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar: ' + str(e))
        return redirect(url_for('formUpdate', id=id))
    finally:
        cursor.close()

#Ruta de detalle
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM BD_Albums WHERE id_Album=%s and State = 1', (id,))
        consultaId= cursor.fetchone()
        return render_template('consulta.html', album= consultaId)
    
    except Exception as e:
        print('Error al consultar por ID: '+e)
        return redirect(url_for('home'))
    
    finally:
        cursor.close()
        
#Ruta para confirmar un delete
@app.route('/confirmarEliminar/<int:id>')
def confirmarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM BD_Albums WHERE id_Album = %s AND State = 1', (id,))
        album = cursor.fetchone()
        if album:
            return render_template('confirmDel.html', album = album)
        else:
            flash('El album no se pudo encontrar o ya se eliminó, NIMODO')
            return redirect(url_for('home'))
    except Exception as e:
        flash('Error: '+ str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()
        
#Ruta para hacer el SOFT DELETE (cambiar state a 0)
@app.route('/eliminarAlbum/<int:id>', methods=['POST'])
def eliminarAlbum(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE BD_Albums SET State = 0 WHERE id_Album = %s', (id,))
        mysql.connection.commit()
        flash('Album eliminado exitosamente :D')
    except Exception as e:
        mysql.connection.rollback()
        flash('Error al eliminar: '+ str(e))
    finally:
        cursor.close()
        return redirect(url_for('home'))

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado, Error de capa 8 !!!',404

@app.errorhandler(405)
def metodonoP(e):
    return 'Revisa el método del enío de tu ruta (GET o POST !!!)',405

#ruta para probar la conexión a MySQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500
    
#Agregar nueva ruta para agregar albums
#Ruta para el Insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    
    #Lista de errores
    errores={}
    
    #Obtener los datos a insertar
    Vtitulo= request.form.get('txtTitulo','').strip()
    Vartista= request.form.get('txtArtista','').strip()
    Vanio= request.form.get('txtAnio','').strip()
    
    if not Vtitulo:
        errores['txtTitulo']= 'Nombre del album obligatorio'
    if not Vartista:
        errores['txtArtista']= 'Nombre del artista obligatorio'
    if not Vanio:
        errores['txtAnio']= 'Año es obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio']= 'Ingresa un año válido'
        
    if not errores:
        #Intentamos ejecutar el inset
        try:
            cursor= mysql.connection.cursor()
            cursor.execute('insert into BD_Albums(album, artista, anio) values(%s,%s,%s)', (Vtitulo, Vartista, Vanio)) #Inserciones de datos
            mysql.connection.commit()
            flash('Album se guardo en BD')
            return redirect(url_for('home'))
        
        except Exception as e:
                mysql.connection.rollback()
                flash('Esta mal en algo, nimodo'+ str(e))
                return redirect(url_for('home'))
            
        finally:
            cursor.close()
    
    return render_template('formulario.html', errores=errores)

if __name__ == '__main__':
    app.run(port=3000,debug=True)