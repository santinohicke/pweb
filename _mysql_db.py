import mysql.connector
from mysql.connector import Error

def conectarBD(configDB=None):
    ''' # Establecer una conexión con el servidor MySQL
        # retorna la conexión
    '''
    mydb=None
    if configDB!=None:
        try:        
            mydb = mysql.connector.connect(
                    host=configDB.get("host"),
                    user=configDB.get("user"),
                    password=configDB.get("pass"),
                    database=configDB.get("dbname")
                   )
        except mysql.connector.Error as e:
            print("ERROR ->",e)        
    return mydb

def cerrarBD(mydb):
    ''' # Realiza el cierra un conexión a una base de datos.
        # recibe 'mydb' una conexion a una base de datos
    '''
    if mydb!=None:
        mydb.close()


def ejecutarDB(mydb,sQuery="",val=None):
    ''' # Realiza las consultas 'INSERT' 'UPDATE' 'DELETE'
        # recibe 'mydb' una conexion a una base de datos
        # recibe 'sQuery' la cadena con la consulta (query) sql.
        # recibe 'val' valores separados anti sql injection
        # retorna la cantidad de filas afectadas con la query.
    '''
    res=None
    try:
        mycursor = mydb.cursor()
        if val==None:
            mycursor.execute(sQuery)
        else:
            mycursor.execute(sQuery,val)
        mydb.commit()   
        res=mycursor.rowcount        # filas afectadas
    except mysql.connector.Error as e:
        mydb.rollback()
        print("ERROR ->",e)    
    return res

def selectDB(configDB=None, sql="", val=None, title=False):
    ''' ########## SELECT
        # recibe 'configDB' un 'dict' con los parámetros de conexión
        # recibe 'sql' una cadena con la consulta SQL
        # recibe 'val' valores separados para prevenir SQL injection
        # recibe 'title' booleana
        # retorna una 'list' con el resultado de la consulta
        #     cada fila de la 'list' es una 'tuple'
        #     Si 'title' es True, entonces agrega a la lista
        #     los títulos de las columnas.
    '''
    resQuery = None
    if configDB is not None:
        connection = conectarBD(configDB)
        if connection is not None:
            resQuery = consultarDB(connection, sQuery=sql, val=val, title=title)
            cerrarBD(connection)
    
    if resQuery is None:
        return []  # Asegura que se devuelvan una lista vacía si no hay resultados
    
    return resQuery



def insertDB(configDB=None,sql="",val=None):
    ''' ########## INSERT
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
    '''
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

def updateDB(configDB=None,sql="",val=None):
    ''' ########## UPDATE
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
    '''
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res

def deleteDB(configDB=None,sql="",val=None):
    ''' ########## DELETE
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
    '''
    res=None
    if configDB!=None:
        mydb=conectarBD(configDB)
        res=ejecutarDB(mydb,sQuery=sql,val=val)
        cerrarBD(mydb)
    return res




def consultarDB(connection, sQuery, val=None, title=False):
    ''' Ejecuta una consulta SELECT y devuelve el resultado'''
    try:
        cursor = connection.cursor()
        cursor.execute(sQuery, val)  # Ejecuta la consulta SQL

        # Si 'title' es True, agregamos los títulos de las columnas a la lista
        if title:
            columns = [desc[0] for desc in cursor.description]
            result = [columns] + cursor.fetchall()
        else:
            result = cursor.fetchall()

        cursor.close()
        return result
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None




configDB={ 
        "host":"localhost",
        "user":"root",
        "pass":"",
        "dbname":"seva"
        }