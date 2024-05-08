import os

pedir = 1
cuenta = 0
pedido_terminado = "SI"
descuento = ""
codigo_descuento = ""
total_productos = 0
pikachu_roll = 0
otaku_roll = 0
pulpo_venenoso_roll = 0
anguila_electrica_roll = 0
descuento_por_codigo = 0

limpiar_pantalla = os.system("cls")
limpiar_pantalla

while pedir == 1:
    print("Bienvenido!\n¿Que deseas?\nMenu:"
    "\n1. Pikachu Roll $4500"
    "\n2. Otaku Roll $5000"
    "\n3. Pulpo Venenoso Roll $5200"
    "\n4. Anguila Eléctrica Roll $4800")

    while pedido_terminado == "SI":
        while True:
            try:
                numero_de_pedido = int(input("\nIngrese la opción que desee agregar a su carrito: "))
                if numero_de_pedido in [1, 2, 3, 4]:
                    break
                else: 
                    print("¡Error! Ingresa un valor entre 1-4")
            except ValueError:
                print("¡Error! Ingresaste un caracter")
        
        if numero_de_pedido == 1:
            print("Sumaste un Pikachu Roll")
            cuenta += 4500
            total_productos += 1
            pikachu_roll += 1
        elif numero_de_pedido == 2:
            print("Sumaste un Otaku Roll a tu carrito")
            cuenta += 5000
            total_productos += 1
            otaku_roll += 1
        elif numero_de_pedido == 3:
            print("Sumaste un Pulpo Venenoso Roll a tu carrito")
            cuenta += 5200
            total_productos += 1
            pulpo_venenoso_roll = +1
        elif numero_de_pedido == 4:
            print("Sumaste un Anguila Eléctrica Roll a tu carrito")
            cuenta += 4800
            total_productos += 1
            anguila_electrica_roll += 1

        while True:
            try:
                pedido_terminado == str((input("\n¿Deseas agregar otro roll a tu pedido? Si/No: "))).upper()
                if pedido_terminado == "SI":
                    break
                elif pedido_terminado == "NO":
                    pedido_terminado == ""
                    print("Seleccionaste no agregar mas rolls a tu carrito")
                    break
                else: 
                    print("¡Error! Debes seleccionar Si/No")
            except ValueError:
                print("¡Error! Ingresaste un numero")

            
    
    while True:
        try:
            descuento == str(input("\n¿Tienes un codigo de descuento?: ")).upper
            if descuento != "SI" or descuento != "NO":
                break
            else: 
                print("¡Error! Debes seleccionar Si/No")
        except ValueError:
            print("¡Error! Ingresaste un numero")

    if descuento == "SI":
        while True:
            try:
                codigo_descuento == str(input("\n¿Cual es el codigo de descuento?: "))
                if codigo_descuento == "soyotaku":
                    descuento_por_codigo = cuenta * 0.1
                    print("Obtuviste un codigo de descuento de 10%")
                    break
                else: 
                    print("Código no válido")
                    while True:
                        try:
                            descuento == str(input("\n ¿Quieres ingresar un codigo nuevamente? Si/No: ")).upper
                            if descuento != "SI" and descuento != "NO":
                                break   
                            else:
                                print("¡Error! Debes ingresar Si/No")
                        except ValueError:
                            print("¡Error! Ingresaste un numero")
                            
            except ValueError:
                print("¡Error! Ingresaste un numero")
            if codigo_descuento == "NO":
                print("No tienes codigo de descuento")
                break
    
    print("****************************************************************"
          f"TOTAL PRODUCTOS: {total_productos}"
          "****************************************************************"
          f"Pikachu Roll: {pikachu_roll}"
          f"Otaku Roll: {otaku_roll}"
          f"Pulpo Venenoso Roll {pulpo_venenoso_roll}"
          f"Anguila Electrica Roll: {anguila_electrica_roll}"
          "****************************************************************"
          f"Subtotal por pagar: {cuenta}"
          f"Descuento por código: {descuento_por_codigo}"
          f"TOTAL: {cuenta - descuento_por_codigo}")
    
    while True:
        try: 
            pedir = str(input("¿Quieres realizar otro pedido? Si/No")).upper
            if pedir == "SI":
                break
            elif pedir == "NO":
                print("Saliste del programa!\n ¿Vuelve pronto!")
                break
            else: 
                print("¡Error! Debes seleccionar Si/No")
        except ValueError:
                print("¡Error! Ingresaste un numero")



    


        
                








            

