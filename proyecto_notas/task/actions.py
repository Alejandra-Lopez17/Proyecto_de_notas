import task.task as model

class actions:
    
    def crear(self, usuario):
        print(f"Vamos a crear una nota para el usuario {usuario[1]}")
        
        titulo = input("Ingresa un título:")
        descripcion = input("Texto de la task:")
        
        task = model.task(usuario[0], titulo, descripcion)
        guardar = task.guardar()
        
        if guardar[0] >= 1:
            print(f"Nota guardada {task.titulo}")
        else:
            print("La nota no fue guardada")
    
    def mostar(self, usuario):
        print(f"Usuario {usuario[1]}, notas =")
        
        task = model.task(usuario[0])
        taskM = task.mostar()
        
        for task in taskM:
            print("###################################")
            print(task[2])
            print(task[2])
            print("###################################")
            
    def eliminar(self):
        pass     