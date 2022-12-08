import mysql.connector

def conectar():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="artirulos-ucoltis",
            port=3308
        )
        print("Tienes una conexion con la base de datos")
    except:
        print("Tienes un error en la base de datos")
    cursor = db.cursor(buffered=True)
    
    return[db,cursor]