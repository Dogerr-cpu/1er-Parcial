while True:
    try:
        numero=int(input("INGRESE UN NUMERO PARA SEGUIR SU SECUENCIA FIBONACCI: "))
        if numero <= 0:
            print("===NO SE PUEDE HACER UNA SECUENCIA FIBONACCI CON 0 O MENOS===")
        else:
            a=0
            b=1
            for i in range (numero):
                print(a)
                c=a+b
                a=b
                b=c
            break
    except ValueError:
        print("INGRESE UN NUMERO ENTERO")
            
    