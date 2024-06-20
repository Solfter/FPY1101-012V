realizar_pedido = True
kilos_gas = 0
menu_de_pedido = True
eleccion_pedido = True
valor_total = 0


while realizar_pedido:
    print("¡ BIENVENIDO A NUESTRA EMPRESA DISTRIBUIDORA DE GAS !\n")

    validar_nombre_cliente = True
    while validar_nombre_cliente:
            nombre_cliente = input("Ingrese su nombre de cliente: ")
            if len(nombre_cliente) < 3:
                print("\nDebes ingresar un nombre con al menos 3 letras: ")
            else:
                 validar_nombre_cliente = False
    
    validar_telefono = True
    while validar_telefono: 
        try:
            numero_telefono = int(input("Ingrese su teléfono de contacto: "))
            if numero_telefono >= 10**7 and numero_telefono < 10**9:
                validar_telefono = False
                break
            else:
                print("\n¡Error! Debes ingresar un número de telefono entre 8 y 9 dígitos: ")
        except ValueError:
             print("\n¡Error! Ingresaste un caracter, debes ingresar un teléfono de entre 8 y 9 dígitos")

    while menu_de_pedido:
        print("\nMenu:"
        "\n1. Compra entrega camión estándar."
        "\n2. Compra entrega carga específica."
        "\n3. Imprimir boleta y cerrar pedido."
        f"\nTienes {kilos_gas} kilos de gas solicitados")
        validar_eleccion_pedido = True
        while validar_eleccion_pedido:
            try:
                eleccion_pedido = int(input("Seleccione su pedido: "))
                if eleccion_pedido >= 1 and eleccion_pedido <= 3:
                    validar_eleccion_pedido = False
                    break
                else:
                    print("\n¡Error! Debes ingresar un valor entre 1 y 4.")
            except ValueError:
                print("\n¡Error! Ingresaste un caracter, debes ingresar un valor entre 1 y 4.")

        if eleccion_pedido == 1:
            print("\nElegiste comprar la entrega de camión estandar")
            validar_cantidad_camiones = True
            while validar_cantidad_camiones:
                try:
                    cantidad_camiones = int(input("Ingresa la cantidad de camiones que quieres: "))
                    if cantidad_camiones <= 0:
                        print("¡Error! Debes ingresar un valor mayor a 0")
                    else:
                        validar_cantidad_camiones = False
                        break
                except ValueError:
                    print("\n¡Error! Ingresaste un caracter, debes ingresar un valor mayor a 0")
            valor_total += cantidad_camiones * 765000
            kilos_gas += cantidad_camiones * 450

            if cantidad_camiones == 1:
                print(f"Ingresaste {cantidad_camiones} camión")
            else:
                print(f"Ingresate {cantidad_camiones} camiones")


        elif eleccion_pedido == 2:
            print("\nElegiste comprar la entrega carga específica")

            validar_cantidad_cilindros = True
            while validar_cantidad_cilindros:
                try:
                    cilindros_5kg = int(input("\nIngresa la cantidad de cilindros de 5 kilos: "))
                    if cilindros_5kg <= 0:
                        print("¡Error! Ingresa una cantidad mayor a 0")
                        continue
                    cilindros_15kg = int(input("Ingresa la cantidad de cilindros de 15 kilos: "))
                    if cilindros_15kg <= 0:
                        print("¡Error! Ingresa una cantidad mayor a 0")
                        continue
                    cilindros_45kg = int(input("Ingresa la cantidad de cilindros de 45 kilos: "))
                    if cilindros_45kg <= 0:
                        print("¡Error! Ingresa una cantidad mayor a 0")
                        continue
                    validar_cantidad_cilindros = False
                except ValueError:
                    print("¡Error! Ingresaste un caracter, deber ingresar un número")
            
            kilos_gas += cilindros_5kg * 5 + cilindros_15kg * 15 + cilindros_45kg * 45
            cantidad_camiones = kilos_gas/450

            if kilos_gas%450 == 0:
                cantidad_camiones = int(cantidad_camiones)
                valor_total += (cantidad_camiones * 765000)
            else:
                print("\n¡No lograste completar un camión! Se te cobrará $1700 por los kilos de gas adicionales y un valor de transporte extra de $100000")
                kilos_gas_adicionales += kilos_gas%450
                print(f"Cantidad de kilos de gas adicionales: {kilos_gas_adicionales}kg") 
                if cantidad_camiones < 1:
                    cantidad_camiones = int(cantidad_camiones) + 1
                    valor_total +=  100000 + kilos_gas_adicionales*1700
                else:
                    cantidad_camiones = int(cantidad_camiones) + 1
                    valor_total += ((cantidad_camiones - 1) * 765000) + 100000 + kilos_gas_adicionales*1700

        elif eleccion_pedido == 3:
            if kilos_gas == 0:
                print("\n¡Error! Debes de realizar algun pedido antes de imprimir boleta")
            else:
                print("\nElegiste imprimir boleta y cerrar pedido")
                menu_de_pedido = False
    

    print(f"\nCliente: \"{nombre_cliente}\""
        f"\nTeléfono: {numero_telefono}"
        f"\nCantidad de kilos: {kilos_gas}"
        f"\nCamiones: {cantidad_camiones}"
        f"\nValor total: ${valor_total}")
    
    validar_realizar_pedido = True
    while validar_realizar_pedido:
        try:
            realizar_pedido = int(input("\n¿Quieres realizar otra cotización? Si(1) / No(2): "))
            if realizar_pedido == 1:
                realizar_pedido = True
                validar_nombre_cliente = True
                validar_telefono = True
                menu_de_pedido = True
                eleccion_pedido = True
                validar_eleccion_pedido = True
                validar_cantidad_camiones = True
                valor_total = 0
                validar_realizar_pedido = True
                kilos_gas = 0
                kilos_gas_adicionales = 0
                break
            elif realizar_pedido == 2:
                print("\nElegiste salir del programa\n¡Vuelve pronto!")
                realizar_pedido = False
                break
            else:
                print("\n¡Error! Debes ingresar Si(1) o No(2)")
        except ValueError:
            print("\n¡Error! Ingresaste un caracter, debes ingresar Si(1) o No(2)")

                


    

            

    
    

    

             
    