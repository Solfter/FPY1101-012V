import os

pedir = 1
cuenta = 0

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
    print("\nBienvenido!\n¿Que deseas?\nMenu:"
    "\n1. Pikachu Roll $4500"
    "\n2. Otaku Roll $5000"
    "\n3. Pulpo Venenoso Roll $5200"
    "\n4. Anguila Eléctrica Roll $4800")
    pedido_terminado = "SI"
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
                pedido_terminado = str.upper((input("\n¿Deseas agregar otro roll a tu pedido? Si/No: ")))
                if pedido_terminado == "SI":
                    break
                elif pedido_terminado == "NO":
                    pedido_terminado == "NO"
                    print("\nSeleccionaste no agregar mas rolls a tu carrito")
                    break
                else: 
                    print("¡Error! Debes seleccionar Si/No")
        
    while True:
        descuento = str.upper((input("\n¿Tienes un codigo de descuento? Si/No: ")))
        if descuento == "SI" or descuento == "NO":
            break
        else: 
            print("¡Error! Debes seleccionar Si/No")

    if descuento == "SI":
        while True:
            codigo_descuento = str(input("\n¿Cual es el codigo de descuento?: "))
            if codigo_descuento == "soyotaku":
                descuento_por_codigo = int(cuenta * 0.1)
                print("Obtuviste un codigo de descuento de 10%")
                break
            else: 
                print("Código no válido")
                while True:
                        descuento = str.upper((input("\n¿Quieres ingresar un codigo nuevamente? Si/No: ")))
                        if descuento == "SI" or descuento == "NO":
                            print(descuento)
                            break 
                        else:
                            print("¡Error! Debes ingresar Si/No")               
            if descuento == "NO":
                print("No tienes codigo de descuento")
                break
    
    print("****************************************************************"
          f"\nTOTAL PRODUCTOS: {total_productos}"
          "\n****************************************************************"
          f"\nPikachu Roll: {pikachu_roll}"
          f"\nOtaku Roll: {otaku_roll}"
          f"\nPulpo Venenoso Roll {pulpo_venenoso_roll}"
          f"\nAnguila Electrica Roll: {anguila_electrica_roll}"
          "\n****************************************************************"
          f"\nSubtotal por pagar: {cuenta}"
          f"\nDescuento por código: {descuento_por_codigo}"
          f"\nTOTAL: {cuenta - descuento_por_codigo}")
    
    while True:
            pedir = str.upper((input("\n¿Quieres realizar otro pedido? Si/No: ")))
            if pedir == "SI":
                pedir = 1
                break
            elif pedir == "NO":
                print("Saliste del programa!\n ¿Vuelve pronto!")
                break
            else: 
                print("¡Error! Debes seleccionar Si/No")




    


        
                








            

