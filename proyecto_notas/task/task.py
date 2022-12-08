import usuario.conexion as conexion

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]

class task:
    
    def __init__(self, usuario_id,titulo="",descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        
    def guardar(self):
        sql = "INSERT INTO task VALUES(null, %s, %s, %s, NOW())"
        task =(self.usuario_id,self.titulo,self.descripcion)
        
        cursor.execute(sql,task)
        db.commit()
        return[cursor.rowcount, self]
    
    def mostar(self):
        sql = f"SELECT * FROM task WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return  result
        

    