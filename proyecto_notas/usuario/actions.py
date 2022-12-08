import usuario.usuario as model
import task.actions

class actions:
    
    def login(self):
        print("¡¡Vamos a iniciar sesión!!")
        try:
            correo = input("Introduce tu correo:")
            passw = input("Introduce tu contraseña:")
            
            usuario = model.Usuario('','',correo, passw)
            
            iniciar = usuario.login()
            
            if correo == iniciar[3]:
                print(f"Felicidades has iniciado sesión {iniciar[1]}, con el correo {iniciar[3]}")
                self.siguenteTarea(iniciar)
        except:
            print("Inicio de sesión fallido")
            
        
    def register(self):
        try:
            print("¡¡Vamos a registarte!!")
            nombre = input("Introduce tu nombre:")
            apellido = input("Introduce tu apellido:")
            correo = input("Introduce tu corre:")
            passw = input("Introduce tu contraseña:")
            
            usuario = model.Usuario(nombre,apellido,correo,passw)
            registro = usuario.register()
            
        except:
            print("Error al registar ")
        
    def siguenteTarea(self, usuario):
        print("""
            Que quiere realizar:
            1. Crear una tarea
            2. Mostar tus tareas
            3. Eliminar una tarea
            4. Cerrar sesión 
            """)
        
        opcion = int(input("Elige una opción: "))
        
        opcionTask = task.actions.actions()

        if opcion == 1:
            opcionTask.crear(usuario)
            self.siguenteTarea(usuario)
        elif opcion == 2:
            opcionTask.mostar(usuario)
            self.siguenteTarea(usuario)
        elif opcion == 3:
            print("Eliminar")
            self.siguenteTarea(usuario)
        elif opcion == 4:
            print("Cerrar sesión")
            exit()
        else:
            print("Opcion no valida")
            self.siguenteTarea(usuario)
            
        