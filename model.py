from _mysql_db import *


def crearUsuario(di):
    '''### Información:
        Agrega un nuevo usuario (un registro) en la tabla usuario de la DB
        Recibe 'di' un diccionario con los datos del usuario a agregar en la tabla.
        Retorna True si realiza con éxito el insert, False caso contrario.
    '''
    sQuery=""" 
        INSERT INTO usuario
        (id, nombre_completo, email, legajo, password, tipo_usuario)
        VALUES
        (%s, %s, %s, %s, %s, %s);
    """
    val = (
        None,  # Para 'id', que es autoincrementable
        di.get('nombre_completo'),  
        di.get('email'),
        di.get('legajo'),
        di.get('contraseña'),
        di.get('tipo_usuario')
    )
    
    # llama a la función para realizar el insert
    resul_insert = insertDB(configDB, sQuery, val) 
    
    # verifica si la inserción fue exitosa
    return resul_insert == 1   

def obtenerID(diRequest):
    if "nombre" in diRequest:
        sql = """
            SELECT id
            FROM aula
            WHERE nombre = %s AND capacidad = %s AND tiene_proyector = %s AND tiene_pc = %s 
        """
        print(diRequest)
        val = (diRequest['nombre'], diRequest['capacidad'], diRequest['proyector'], diRequest['pc'])
        print(val)
        resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
        print(resQuery)
        if resQuery:
            return resQuery[0][0]
        else:
            return None
    elif "materias" in diRequest:   
        sql = """
            SELECT id
            FROM materia
            WHERE nombre_materia = %s
        """
        val = (diRequest['materias'],)
        resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
        print(resQuery)
        print(resQuery)
        print(resQuery)
        if resQuery:
            return resQuery[0][0]
        else:
            return None

def validarUsuarioProfe(email, password, legajo):
    
    '''### Información:
          Se consulta a la BD un usuario 'email', 'contraseña' y 'legajo'
          retorna True si 'email', 'contraseña' y 'legajo' son válidos
          retorna False caso contrario
    '''
    sSql = '''
        SELECT * FROM usuario
        WHERE 
            email = %s
        AND 
            password = %s
        AND 
            legajo = %s
        AND 
            tipo_usuario = 'profesor';
    '''
    val = (email, password, legajo)
    fila = selectDB(configDB=configDB, sql=sSql, val=val)
    
    return len(fila) > 0  # Devuelve True si hay un resultado, de lo contrario False

def validarUsuarioAlumno(email, password, legajo):
    
    '''### Información:
          Se consulta a la BD un usuario 'email', 'contraseña' y 'legajo'
          retorna True si 'email', 'contraseña' y 'legajo' son válidos
          retorna False caso contrario
    '''
    sSql = '''
        SELECT * FROM usuario
        WHERE 
            email = %s
        AND 
            password = %s
        AND 
            legajo = %s
        AND 
            tipo_usuario = 'alumno';
    '''
    val = (email, password, legajo)
    fila = selectDB(configDB=configDB, sql=sSql, val=val)
    
    return len(fila) > 0  

def validarUsuarioAdmin(email, password, legajo):
    
    '''### Información:
          Se consulta a la BD un usuario 'email', 'contraseña' y 'legajo'
          retorna True si 'email', 'contraseña' y 'legajo' son válidos
          retorna False caso contrario
    '''
    sSql = '''
        SELECT * FROM usuario
        WHERE 
            email = %s
        AND 
            password = %s
        AND 
            legajo = %s
        AND 
            tipo_usuario = 'admin';
    '''
    val = (email, password, legajo)
    print(val)
    fila = selectDB(configDB=configDB, sql=sSql, val=val)
    
    return len(fila) > 0  # Devuelve True si hay un resultado, de lo contrario False

def seleccionComisiones(id_profe):
    sql = """
        SELECT id_aula, id_materia, id_profesor, dias, horario
        FROM comision
        WHERE id_profesor = %s
    """
    val = (id_profe,)  # Asegúrate de que 'val' sea una tupla
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery

def encontrarComisionAlumno(id_comision):
    sql = """
        SELECT id_aula, id_materia, id_profesor, dias, horario
        FROM comision
        WHERE id = %s
    """
    val = (id_comision,)  # Asegúrate de que 'val' sea una tupla
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery

def inscripcionAlumno(id_alumno):
    sql = """
        SELECT id, id_alumno, id_comision
        FROM inscripcion
        WHERE id_alumno = %s
    """
    val = (id_alumno,)  # Asegúrate de que 'val' sea una tupla
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery

def comisionIDmat(id_materia):
    sql = """
        SELECT id_aula, id_materia, id_profesor, dias, horario
        FROM comision
        WHERE id_materia = %s
    """
    val = (id_materia,)  # Asegúrate de que 'val' sea una tupla
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery
    
def comision(id_profesor, id_aula, id_materia, dias, horario):
    print(id_profesor, id_aula, id_materia, dias, horario)
    sql = """
        INSERT INTO comision (id_profesor, id_aula, id_materia, dias, horario)
        VALUES (%s, %s, %s, %s, %s)
    """
    val = (id_profesor, id_aula, id_materia, dias, horario)
    res = insertDB(configDB=configDB, sql=sql, val=val)
    return res

def obtenerUsuarioXEmailPass(result, email, password):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'
       y del 'password'.
       Carga la información obtenida de la BD en el dict 'result'.
       Recibe 'result' en diccionario donde se almacena la respuesta de la consulta.
       Recibe 'email' que es el mail si se utiliza como clave en la búsqueda.
       Recibe 'password' que se utiliza en la consulta. (Para validar al usuario).
       Retorna:
        True cuando se obtiene un registro de usuario a partir del 'email' y el 'password'.
        False caso contrario.
    '''
    
    res = False
    sSql = """SELECT id, nombre_completo, email, legajo, password, tipo_usuario 
              FROM usuario WHERE email = %s AND password = %s;"""
    val = (email,password,)
    
    # Ejecutamos la consulta a la base de datos
    fila = selectDB(configDB, sSql, val)
    
    if fila != []:
        # Obtener la contraseña almacenada en la base de datos
        stored_password = fila[0][4]  # La contraseña guardada en la BD
        
        # Comparar las contraseñas (si están en texto plano)
        if password == stored_password:
            res = True
            result['id'] = fila[0][0]
            result['nombre_completo'] = fila[0][1]
            result['email'] = fila[0][2]
            result['legajo'] = fila[0][3]
            result['password'] = fila[0][4]
            result['tipo_usuario'] = fila[0][5]
        else:
            print("Contraseña incorrecta.")
    else:
        print("No se encontró el email en la base de datos.")
    
    return res


def obtenerMateria(id):
    sql = """
        SELECT nombre_materia
        FROM materia
        WHERE id = %s
    """
    val = (id,)
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery[0][0]

def obtenerAula(id):

    sql = """
        SELECT nombre
        FROM aula
        WHERE id = %s
    """
    val = (id,)
    resQuery = selectDB(configDB=configDB, sql=sql, val=val, title=False)
    return resQuery[0][0]

def seleccionMaterias():

    sql = """
        SELECT nombre_materia
        FROM materia
    """
    resQuery = selectDB(configDB=configDB, sql=sql, val=None, title=False)
    return resQuery

def borrarMateria(materia):
    a=materia
    print(a)
    sql = """
        DELETE FROM materia
        WHERE nombre_materia = %s
    """
    
    val = (materia,)
    print(val)
    res = deleteDB(configDB=configDB, sql=sql, val=val)
    print(res)
    return res
        
def añadirMateria(materia):

    sql= """
        INSERT INTO materia (nombre_materia)
        VALUES (%s)
    """
    
    val=(materia,)
    res = insertDB(configDB=configDB, sql=sql, val=val)
    return res

def aulasAdmin():

    sql= """
        SELECT * 
        FROM aula
    """
    resQuerry= selectDB(configDB=configDB, sql=sql, val=None)
    print(resQuerry)
    return resQuerry

def aulasProfe():

    sql="""
        SELECT * 
        FROM aula
    """

    resQuerry = selectDB(configDB=configDB, sql=sql, val=None)
    print(resQuerry)
    return resQuerry

def obtenerMat_id(materia):

    sql="""
        SELECT id 
        FROM materia
        WHERE nombre_materia=%s
    """

    val=(materia,)
    resQuerry= selectDB(configDB=configDB, sql=sql, val=val)
    return resQuerry

def obtenerAula_id(aula):

    sql="""
        SELECT id 
        FROM aula
        WHERE nombre=%s
    """
    val=(aula,)
    resQuerry=selectDB(configDB=configDB, sql=sql, val=val)

    return resQuerry

def comisionInscripcion(id_materia, id_aula, dias, horario):
    
    sql = """
        SELECT id FROM comision 
        WHERE id_aula=%s AND id_materia=%s AND dias=%s AND horario=%s
        
    """
    val = ( id_aula, id_materia, dias, horario)
    resQuerry = selectDB(configDB=configDB, sql=sql, val=val)
    
    return resQuerry

def inscripto(id_usuario,id_comision):

    sql="""
        INSERT INTO inscripcion ( id_alumno, id_comision)
        VALUES (%s, %s)
    """
    val=(id_usuario,id_comision)
    resQuerry=insertDB(configDB=configDB, sql=sql, val=val)
    return resQuerry

def guardarAulaAdmin(nombre,capacidad,proyector, computadoras):

    sql="""
        INSERT INTO aula (nombre, capacidad, tiene_pc, tiene_proyector)
        VALUES (%s, %s, %s, %s)
    """

    val=(nombre,capacidad,computadoras,proyector)
    resQuerry=insertDB(configDB=configDB, sql=sql, val=val)
    return resQuerry