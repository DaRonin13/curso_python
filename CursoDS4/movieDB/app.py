''' Program principal de MovieDB '''
from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import os
import movie_classes as mc
 
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secreto para la sesión
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
relaciones_csv = ruta + 'relacion.csv'
users_csv = ruta + 'users_hashed.csv'
sistema.cargar_csv(actores_csv,mc.Actor)
sistema.cargar_csv(peliculas_csv,mc.Pelicula)
sistema.cargar_csv(relaciones_csv,mc.Relacion)
sistema.cargar_csv(users_csv,mc.User)
 
@app.route('/')
def index():
    return render_template('base.html')
 
@app.route('/actores')
def actores():
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)
 
@app.route('/peliculas')
def peliculas():
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)
 
@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    ''' Muestra la informacion de un actor '''
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    ''' Muestra la informacion de una pelicula '''
    pelicula = sistema.peliculas[id_pelicula]
    actores = sistema.obtener_actores_por_pelicula(id_pelicula)
    return render_template('pelicula.html', pelicula=pelicula, lista_actores=actores)

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Muestra el formulario de login '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito = sistema.login(username, password)
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos'
            return render_template('login.html')
    return render_template('login.html')
 
if __name__ == '__main__':
    app.run(debug=True)