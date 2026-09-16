try:
    vehiculo=int(input("Ingrese el tipo de vehículo (1 para automóvil, 2 para motocicleta, 3 para camión): "))
    tarifa=0
    match vehiculo:
        case 1:
            tarifa= 10
            vehiculo="Automovil"
            print(f"El tipo de vehículo es automóvil y la tarifa es de: {tarifa} %")
        case 2:
            tarifa= 5
            Vehiculo="Motocicleta"
            print(f"El tipo de vehículo es motocicleta y la tarifa es de: {tarifa} %")
        case 3:
            tarifa= 20
            Vehiculo="Camion"
            print(f"El tipo de vehículo es camión y la tarifa es de: {tarifa} %")
        case _:
            print("Tipo de vehículo no válido.")
            exit()
except ValueError:
    print("INGRESE UN NUMERO PARA ELEGIR SU OPCION")
try:
    hora= int(input("Cuantas horas estuvo parqueado? : "))
    if hora <= 0:
        print("INGRESE UNA HORA VALIDA DEBE SER MAYOR A 0")
    elif hora > 4:
        recargo=tarifa*0.15
        tarifa_final=tarifa+recargo
        print(f"""
            tipo de vehiculo: {vehiculo}
            tarifa normal= {tarifa}
            tarifa con recargo de 4 horas: {tarifa_final}""")
    else:
        print(f"""
                tipo de vehiculo: {vehiculo}
                tarifa normal= {tarifa}""")
except ValueError:
    print("INGRESE UN NUMERO ENTERO")