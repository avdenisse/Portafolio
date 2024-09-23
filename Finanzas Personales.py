# Este programa mira tus finanzas personales. Puedes agregar, restar, ver tus compras y el total en tu cuenta.

# Listas para almacenar la información de cuenta y compras
cuenta = []
compras = []
gasto = []

# Bucle principal
while True:
    # Menú de opciones
    print(''' 
                         *************************************************
                         *           $ Finanzas Personales $             *
                         *                                               *
                         *                    Menu                       *
                         *             1. Agregar a tu cuenta            *
                         *             2. Sacar de tu cuenta             *
                         *             3. Ver compras realizadas         *
                         *             4. Ver total en tu cuenta         *
                         *             5. Salir                          * 
                         *                                               *
                         *************************************************
      ''')

    # Solicitar opción del usuario
    try:
        opc = int(input('Digite su opción: '))
    except ValueError:
        print("Por favor, ingrese una opción válida.")
        continue

    # Opción 1: Agregar dinero a la cuenta
    if opc == 1:
        try:
            cantidad = int(input('Ingrese cantidad a agregar: '))
            print(f'Agregaste {cantidad} a tu cuenta.')
            cuenta.append(cantidad)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    
    # Opción 2: Registrar una compra
    elif opc == 2:
        item = input('Ingrese el producto que compró: ')
        try:
            costo = int(input('Ingrese el precio del producto: '))
            print(f'''
            ****************************************
                             Recibo
                     Compraste: {item}
                     Precio: {costo}
            ****************************************
            ''')
            compras.append((item, costo))  # Guardar el item y su costo
            gasto.append(costo)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.")

    # Opción 3: Ver compras realizadas
    elif opc == 3:
        if compras:
            print('''
            ***********************************************************************************
                             Las compras realizadas fueron las siguientes:                             
            ''')
            for i, (item, costo) in enumerate(compras, 1):
                print(f'{i}. Producto: {item} - Precio: {costo}')
            print('***********************************************************************************')
        else:
            print("No has realizado compras aún.")
    
    # Opción 4: Ver total en la cuenta
    elif opc == 4:
        sumacuenta = sum(cuenta)
        sumagasto = sum(gasto)
        total = sumacuenta - sumagasto
        print(f'''
        ***************************************************************************************
              Tienes en tu cuenta: {total}
        ***************************************************************************************
        ''')

    # Opción 5: Salir del programa
    elif opc == 5:
        print('Fin del Programa. ¡Hasta pronto!')
        break

    # Si la opción no es válida
    else:
        print("Opción no válida. Inténtalo de nuevo.")
