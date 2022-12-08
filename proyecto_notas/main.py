from usuario import actions

print("Bienvenido a la aplicación task coltis")
print("Elige una opción:")
print("1. Login")
print("2. Registro")
opcion = int(input())
    
acci = actions.actions()
if opcion == 1:
    acci.login()
elif opcion == 2:
    acci.register()
else:
    print("Opcion no valida")