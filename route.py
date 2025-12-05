from flask import Flask, render_template, request, redirect, session, flash, url_for  
from appConfig import config 
from uuid import uuid4 
from werkzeug.utils import secure_filename
from controller import *
import os


def route(app):

    #rutas:
    
    
    @app.route('/')   # decordador
    def index():
        return render_template('index.html')
    
    @app.route('/login_a',methods=['POST', 'GET'])
    def loginA():
        direquest = {}
        getRequest(direquest) 
        if request.method == 'POST':
            return procesarAccesoAlumno(direquest)  
        else:
            return render_template('login-a.html')
        
        

    @app.route('/login_adm',methods=['POST', 'GET'])
    def loginAdm():
        direquest = {}
        getRequest(direquest) 
        if request.method == 'POST':
            return procesarAccesoAdmin(direquest)  
        else:
            return render_template('login-adm.html')
    
    @app.route('/login_profe', methods=['POST', 'GET'])
    def loginProf():
        direquest = {}
        getRequest(direquest) 
        print(direquest)
        if request.method == 'POST':
            return procesarAccesoProfe(direquest)  
        else:
            return render_template('login-profe.html')   
   
    

    
    @app.route('/creacion_alumnos_admin') 
    def creacionAlumnosAdmin():
        if haySesion() and session.get('rol') == 'admin':
            return render_template('usuarios-admin.html')
        else:
            return render_template('index.html')
    
    
    @app.route('/inicio_alumno')
    def inicioA():
        if haySesion() and session.get('rol') == 'alumno':
            return render_template('inicio-alumno.html')
        else:
            return render_template('index.html')
    
    @app.route('/inicio_admin')
    def inicioAdm():
        if haySesion() and session.get('rol') == 'admin':
            return render_template('inicio-admin.html')
        else:
            return render_template('index.html')
    
    
    @app.route('/inicio_profe')
    def inicioProf():
        if haySesion() and session.get('rol') == 'profesor':
            return render_template('inicio-profe.html')
        else:
            return render_template('index.html')
    
    
    #creacion usuarios-admin
    @app.route('/recibir_datos',methods=['POST', 'GET'])  
    def formrecibe():
        if haySesion() and session.get('rol') == 'admin':
            diRequest={}            
            getRequest(diRequest)   
            return registrarUsuario(diRequest)
        else:
            return render_template('index.html')
    

    @app.route('/aulas-admin')
    def aulasAdministrador():
        if haySesion() and session.get('rol') == 'admin':
            return obtenerAulasAdmin()
        else:
            return render_template('index.html')
    
    
    @app.route('/reservas-profesor', methods=['POST', 'GET'])
    def aulasProfeReserva():
        if haySesion() and session.get('rol') == 'profesor':
            diRequest = {}
            getRequest(diRequest)
            print(diRequest)
            session["id_aula"]=idAula(diRequest)
            print(session)
            return añadircomision()
        else:
            return render_template('index.html')
       
    @app.route('/agregar-aulas-admin')
    def agregarAulas():
        if haySesion() and session.get('rol') == 'admin':
            return render_template('editar-aulas.html')
        else:
            return render_template('index.html')

    @app.route('/editar-aulas')
    def editarAulas():
        if haySesion() and session.get('rol') == 'admin':
            diRequest={}
            getRequest(diRequest)
            print(diRequest)
            return guardarAula(diRequest)
        else:
            return render_template('index.html')
    
    @app.route('/inscribirse-alumno', methods=['POST', 'GET'])
    def inscribirAlumno():
        if haySesion() and session.get('rol') == 'alumno':
            diRequest = {}
            getRequest(diRequest)
            session['id_materia'] = idMateria(diRequest)
            print(session)
                
            return comiAlum(session['id_materia'])
        else:
            return render_template('index.html')
        
        
    
    @app.route('/datos-inscripcion-alumno', methods=['POST', 'GET'])
    def inscribirse_alumno():
        if haySesion() and session.get('rol') == 'alumno':
            diRequest = {}
            getRequest(diRequest)
            return comiAlum(session['id_materia'])
        else:
            return render_template('index.html')
        

    @app.route('/materias-admin')
    def materiasAdmin():
        if haySesion() and session.get('rol') == 'admin':
            return obtenerMaterias()
        else:
            return render_template('index.html')
        
    
    @app.route('/materias-profesor')
    def materiasProfesor():
        if haySesion() and session.get('rol') == 'profesor':
            return obtenerMateriasProfe()
        else:
            return render_template('index.html')
    
    @app.route('/materias-alumno')
    def materiasAlumno():
        if haySesion() and session.get('rol') == 'alumno':
            return obtenerMateriasAlumno()
        else:
            return render_template('index.html')
    
    @app.route('/perfil-admin')
    def perfilAdmin():
        if haySesion() and session.get('rol') == 'admin':
            diRequest = {}
            getRequest(diRequest)
            nombre = session['nombre']
            email = session['email']
            return render_template('perfil-admin.html',nombre=nombre,email=email)
        else:
            return render_template('index.html')
    




    
    @app.route('/perfil-alumno')
    def perfil_alumno():
        if haySesion() and session.get('rol') == 'alumno':
            diRequest = {}
            getRequest(diRequest)
            
            id_alumno = session['id_usuario']
            return obtenerinscripcion(id_alumno)
        else:
            return render_template('index.html')
        
    
    @app.route('/perfil-profesor')
    def perfil_profe():
        if haySesion() and session.get('rol') == 'profesor':
            diRequest = {}
            getRequest(diRequest)
            nombre = session['nombre']
            email = session['email']
            id_profe = session['id_usuario']
            return obtenerComisiones(id_profe)
        else:
            return render_template('index.html')
        
    
    @app.route('/logout', methods=['POST', 'GET'])
    def cerrarsession():
        
        return logout()

    
    
    
    @app.route('/inscribirse-profesor', methods=['POST', 'GET'])
    def datos():
        if haySesion() and session.get('rol') == 'profesor':
            diRequest = {}
            getRequest(diRequest)
            print(diRequest)
            session['id_materia'] = idMateria(diRequest)
            return inscProf()
        else:
            return render_template('index.html')
    

    @app.route('/datos-inscripcion-profe', methods=['POST', 'GET'])
    def inscribirse_profe():
        if haySesion() and session.get('rol') == 'profesor':
            diRequest = {}
            getRequest(diRequest)
            session["fecha-hora"]=diRequest
            print(diRequest)
            return obtenerAulasProfe()
        else:
            return render_template('index.html')
    
    @app.route('/datos-agregar-materia', methods=['POST','GET'])
    def agregarMaterias():
        if haySesion() and session.get('rol') == 'admin':
            diRequest = {}
            getRequest(diRequest)
            print(diRequest)
            agregarmateria(diRequest)
            return redirect('/materias-admin')
        else:
            return render_template('index.html')


    @app.route('/agregar-materia')
    def agregarMat():
        if haySesion() and session.get('rol') == 'admin':
            return render_template('agregar-materias.html')
        else:
            return render_template('index.html')

    @app.route('/modificacion-materia', methods=['POST', 'GET'])
    def editEimmaterias():
        if haySesion() and session.get('rol') == 'admin':
            diRequest = {}
            getRequest(diRequest)
            print(diRequest)
            eliminarMateria(diRequest)
            return redirect('/materias-admin')
        else:
            return render_template('index.html')    

    @app.route('/inscripcion-ALUMNO', methods=['POST', 'GET'])
    def inscribirseALUMNO():
        if haySesion() and session.get('rol') == 'alumno':
            diRequest={}
            getRequest(diRequest)
            print(diRequest)
            return comisionesAlumnos(diRequest)
        else:
            return render_template('index.html')