#Realizado por silvia Cerdas

#Realiza la lista de productos
menu = ["Pizza","Hamburguesa","Ensalada","Refresco","Papas","Postre","Te",
        "Flan"]

#Realiza el diccionario de productos
precios_menu ={"Pizza":25.7,"Hamburguesa":12.5,"Ensalada":5.5,
                "Papas":6.8,"Refresco":3.2,"Postre":12.6,"Te":4.5,
                "Flan":5.4}

#Realiza diccionario para categorias
categoria_producto= {"Pizza":"Comida", 
                     "Hamburguesa":"Comida",
                     "Ensalada":"Comida",
                     "Refresco":"Bebida",
                     "Papas":"Comida",
                     "Postre":"Postre",
                     "Te":"Bebida",
                     "Flan":"Postre"}

#Realiza  para luego rellenar con el pedido realizado
pedido=[]

#Crea bucle para el desarrollo de pedidos o no 
while True:
    print(f"\n Bienvenido Nuestro Menú es:")
    #Crea para mostrar productos disponibles en el menú
    for x in menu:
            print(f"{x}")
    #Realiza para  notificar al usuario
    print(f"\n Si no desea realizar pedido escribir: salir")
    
    #Realiza la opción  de ingreso de producto o salida del bucle
    opcion= input("Ingrese que producto desea agregar o salir: ")
    
    #Salida del bucle, se coloca el casefold para evitar errores
    if opcion.casefold()=="salir".casefold():
        break
    
    #Realiza la solicitud de pedidos
    elif opcion in precios_menu:
        pedido.append(opcion)
        print(f"El producto se agregó al pedido{pedido}")
    else:
        print(f"Valor no valido")


if not pedido:
    print("\n No se efectuó pedido en este momento")
# Realiza para efectuar la siguiente parte del programa     
else:
    print(f"\n El pedido realizado es: {pedido}")
    total_neto=sum(precios_menu[i] for i in pedido)
    
   #Realiza para establecer los rangos de descuento y valor de este
    if total_neto>50:
        descuento ="10%"
        desc = 0.10

    elif 50>=total_neto>30:
        descuento ="5%"
        desc = 0.05
        
    else:
        descuento ="0%"
        desc = 0.00
        
    #Realiza para poner realizar el bucle con contadores en cero 
    productos_pedidos= {}
    categoria=set()
    
    #Realiza bucle para agregar los productos  del pedido a las categoria
    for producto in pedido:
       productos_pedidos[producto] =productos_pedidos.get(producto,0)+1
       categoria.add(categoria_producto[producto])
       
    #Realiza para poder hacer un bucle con los productos con sus categorias 
    # y cantidades solicitadas
    for producto, cantidad in productos_pedidos.items():
            print(f"*{cantidad} {categoria_producto[producto]}: {producto}")               
    
    #Realiza para obtener precio aplicando el descuento            
    total_pagar = total_neto-(total_neto*desc)
    #Se imprime  los precios con y sin descuento, 
    #junto con el descuento aplicado
    print(f"\n -----Resumen-----")
    print(f"Total neto a pagar es de: ${total_neto:.2f}")
    print(f"El descuento aplicado es de: {descuento}")
    print(f"El total a pagar  con descuento aplicado es: ${total_pagar:.2f}")
    
       