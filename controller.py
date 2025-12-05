from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config



def getRequest(diResult):  
    if request.method=='POST':                     # Si el método de la solicitud es POST
        for name in request.form.to_dict().keys():  # Itera sobre las claves del formulario
            li=request.form.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.form.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""                   # Almacena una cadena vacía en el diccionario
                
    elif request.method=='GET':                   # Si el método de la solicitud es GET
        for name in request.args.to_dict().keys():  # Itera sobre las claves de los argumentos
            li=request.args.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.args.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""
    
def obtenerComisiones(id_profe):
    val= seleccionComisiones(id_profe)  #f en model, lista de tuplas, va a tener ids
    lst=[]
    for item in val:                
        aula=obtenerAula(item[0])         #en model, convierte el id en el nombre del aulq
        materia=obtenerMateria(item[1])         #en model,  " 
        res=(materia,aula,item[3],item[4])      #materia, aula, dia y horario
        lst.append(res)


    nombre = session['nombre']
    email = session['email']
    return render_template('perfil-profe.html', nombre=nombre, email=email, comision=lst)

def procesarAccesoAdmin(direquest):
    
    param = {}
     
    if validarUsuarioAdmin(direquest['email'], direquest['password'], direquest['legajo']):
        crearSesion(direquest)
        return redirect('/inicio_admin')
    else:
        param['error_msj_login'] = "Error: Email o contraseña inválidos"
        return render_template('login-adm.html', param = param)

def procesarAccesoAlumno(direquest):  
    
    param = {}
    
    if validarUsuarioAlumno(direquest['email'], direquest['password'], direquest['legajo']):
        crearSesion(direquest)
        return render_template('inicio-alumno.html')
    else:
        param['error_msj_login'] = "Error: Email o contraseña inválidos"
        return render_template('login-a.html', param = param)

def procesarAccesoProfe(direquest):
    
    param = {}
     
    if validarUsuarioProfe(direquest['email'], direquest['password'], direquest['legajo']):
        crearSesion(direquest)
        return render_template('inicio-profe.html')
    else:
        param['error_msj_login'] = "Error: Email o contraseña inválidos"
        return render_template('login-profe.html', param = param)

def comiAlum(id_materia):
    comisiones = comisionIDmat(id_materia)
    lst=[]
    for item in comisiones:
        aula=obtenerAula(item[0])
        materia=obtenerMateria(item[1])
        res=(materia,aula,item[3],item[4])
        lst.append(res)
    
    return render_template('inscribirse-alumno.html',comision=lst)

def obtenerinscripcion(id_alumno):
    inscripciones = inscripcionAlumno(id_alumno)
    lst=[]
    for item in inscripciones:
        comision = encontrarComisionAlumno(item[2])
        
        aula=obtenerAula(comision[0][0])
        materia=obtenerMateria(comision[0][1])
        res=(materia,aula,comision[0][3],comision[0][4])
        lst.append(res)
    
    nombre = session['nombre']
    email = session['email']
    id_alumno = session['id_usuario']
    return render_template('perfil-alumno.html', nombre=nombre, email=email, inscripciones=lst)
        
def logout():
    cerrarSesion()
    print("Sesión cerrada con éxito.")
    
    return redirect('/')

def idMateria(diRequest):
    id_materia = obtenerID(diRequest)
    return id_materia

def idAula(diRequest):
    id_aula = obtenerID(diRequest)
    return id_aula

     
def añadircomision():
    id_usuario = session['id_usuario']
    id_aula = session['id_aula']
    id_materia = session['id_materia']
    dias = session['fecha-hora']['día']
    hora = session['fecha-hora']['horario']
    
    comision(id_usuario, id_aula, id_materia, dias, hora)
    return render_template("inicio-profe.html")
    
def cargarSesion(dicUsuario):

    '''info:
        Realiza la carga de datos del usuario
        en la variable global dict 'session'.
        recibe 'dicUsuario' que es un diccionario con datos
               de un usuario.
        Comentario: Usted puede agregar en 'session' las claves que necesite
    '''
    session['id_usuario'] = dicUsuario['id']
    session['email'] = dicUsuario['email']  # es el mail
    session['password'] = dicUsuario['password']
    session['nombre'] = dicUsuario['nombre_completo']
    session['rol'] = dicUsuario['tipo_usuario']
    session["time"] = datetime.now()  
    print("Sesión creada con éxito:", session)
    return session

def crearSesion(direquest):
    '''info:
        Crea una sesion. Consulta si los datos recibidos son validos.
        Si son validos carga una sesion con los datos del usuario.
        recibe 'direquest' un diccionario con los datos 'email' y 'password' de un usuario.
        retorna True si se logra una sesion, False caso contrario.
    '''
    sesionValida = False
    dicUsuario = {}
    try: 
        if obtenerUsuarioXEmailPass(dicUsuario, direquest.get("email"), direquest.get("password")):
            cargarSesion(dicUsuario)
            sesionValida = True
    except ValueError:                              
        pass
    return sesionValida

def haySesion():  
    '''info:
        Determina si hay una sesion activa observando si en el dict
        session se encuentra la clave 'username'
        retorna True si hay sesión y False si no la hay.
    '''
    return session.get("id_usuario")!=None

def cerrarSesion():
    '''info:
        Borra el contenido del dict 'session'
    '''
    try:    
        session.clear()
    except:
        pass

def registrarUsuario(diRequest):
    '''Recibe el diccionario con los datos del usuario y lo registra en la base de datos'''

    if crearUsuario(diRequest):
        return render_template('inicio-admin.html')
    else:
        return render_template('usuarios-admin.html')

def obtenerMaterias():

    materias = seleccionMaterias()
    
    return render_template('materias-admin.html', materias=materias)

def obtenerMateriasProfe():
    materias = seleccionMaterias()
    print(materias)
    return render_template('materias-profe.html', materias=materias)

def obtenerMateriasAlumno():
    materias = seleccionMaterias()
    print(materias)
    return render_template('materias-alumno.html',materias=materias)

def eliminarMateria(diRequest):
    materia=diRequest['eliminar']
    
    if borrarMateria(materia):
        print("Materia eliminada corectamente")
    else:
        print("Error al eliminar la materia")
    
def agregarmateria(diRequest):
    materia=diRequest["nombre-materia"]
    
    añadirMateria(materia)
    return redirect('/materias-admin')
    
def obtenerAulasAdmin():
    aulas = aulasAdmin()
    
    return render_template('aulas-admin.html', aulas=aulas)

def obtenerAulasProfe():
    aulas = aulasProfe()
    
    return render_template('aulas-profe-reserva.html', aulas=aulas)

def inscProf():

    return render_template('inscribirse-profe.html')

def comisionesAlumnos(diRequest):
    id_materia= obtenerMat_id(diRequest['materia'])[0][0]  #te devuleve una lista de tuplas
    id_aula= obtenerAula_id(diRequest['aula'])[0][0]
    dias= diRequest['dia']
    hora=diRequest['hora']
    id_comision=comisionInscripcion(id_materia, id_aula, dias, hora)
    inscripto(session['id_usuario'],id_comision[0][0])
    return render_template('inicio-alumno.html')
    
def guardarAula(diRequest):
    nombre=diRequest['nombre-aula']
    capacidad=diRequest['capacidad-aula']
    proyector=diRequest['proyector-aula']
    computadoras=diRequest['computadoras-aula']
    guardarAulaAdmin(nombre,capacidad,proyector, computadoras)
    return redirect('/aulas-admin')