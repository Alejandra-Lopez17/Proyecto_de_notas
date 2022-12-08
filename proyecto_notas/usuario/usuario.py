from datetime import date
import hashlib
import usuario.conexion as conexion

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, correo, passw):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.passw = passw
        
    def register(self):
        fecha = date.today()
        
        encriptar = hashlib.sha256()
        encriptar.update(self.passw.encode('utf8'))
        
        sql = "INSERT INTO usuario VALUES(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellido, self.correo, encriptar.hexdigest(), fecha)
        
        try:
            cursor.execute(sql,usuario)
            db.commit()
            return[cursor.rowcount, self]
        except:
            return[0, self]

    
    def login(self):
        sql = "SELECT * FROM usuario WHERE correo = %s AND passw = %s"
    
        encriptar = hashlib.sha256()
        encriptar.update(self.passw.encode('utf8'))
        
        usuario = (self.correo, encriptar.hexdigest())
        
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        
        return  result
    