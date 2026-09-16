try:
    numero=int(input("INGRESE UN NUMERO ENTRE EL 1-10: "))
    if numero > 1 and numero < 10:
        numero+=1
        for i in range (1,numero):
            print(f"===TABLA DEL {i}===")
            suma=0
            for f in range (1,13):
                x=i*f
                suma+=x
                print(f"{i} x {f} = {x}")
            print(f"LA SUMA DE LOS RESULTADOS DE ESTA TABLA ES: {suma}")
    else:
        print("INGRESE UN NUMERO EN EL RANGO DE 1-10")
except ValueError:
    print("INGRESE UN NUMERO ENTERO")