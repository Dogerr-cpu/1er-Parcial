from Validador import verificar_acceso

def main():
    try:
        Usuario=input("INGRESE SU USUARIO: ").lower().strip()
        Contraseña=input("INGRESE SU CONTRASEÑA: ")
        tipo=verificar_acceso(Usuario,Contraseña)

        if tipo == True:
            print("ACCESO CONCEDIDO")
        elif tipo == False:
            print("CREDENCIALES INCORRECTAS")
    except:
        print("INGRESE DATOS QUE NO ROMPAN EL SISTEMA")

main()