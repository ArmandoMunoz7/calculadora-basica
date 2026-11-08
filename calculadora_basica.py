print("======= CALCULADORA BASICA =======")
print("\n**** MENU DE OPERACIONES ****\n1. SUMA\n2. RESTA\n3. MULTIPLICACION\n4. DIVISION\n5. EXPONENTE\n6. RAIZ CUADRADA\n7. SALIR")
print("----------------------------------------------")
while True:

    while True:
        try:
            selec = int(input("\nNUMERO DE OPERACION A REALIZAR: "))
            if selec <= 0:
                print("\nINGRESA UN NUMERO VÁLIDO")
                continue
            break
        except ValueError:
            print("\nSELECCIONA UNA OPCION VALIDA DEL MENU")

    match selec:
        
        case 1:
            print("\n---- SUMA ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    sum1 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL PRIMER NUMERO VALIDO")

            print("+")

            while True:
                try:
                    sum2 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL SEGUNDO NUMERO VALIDO")

            print(f"= {sum1 + sum2:.2f}")

        case 2:
            print("\n---- RESTA ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    rest1 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL PRIMER NUMERO VALIDO")

            print("-")

            while True:
                try:
                    rest2 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL SEGUNDO NUMERO VALIDO")

            print(f"= {rest1 - rest2:.2f}")

        case 3:
            print("\n---- MULTIPLICACION ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    mult1 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL PRIMER NUMERO VALIDO")

            print("X")

            while True:
                try:
                    mult2 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL SEGUNDO NUMERO VALIDO")

            print(f"= {mult1 * mult2:.2f}")

        case 4:
            print("\n---- DIVISION ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    div1 = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL PRIMER NUMERO VALIDO")

            print("/")

            while True:
                try:
                    div2 = float(input(""))
                    if div2 == 0:
                        print("NO SE PUEDE DIVIDIR ENTRE 0. INTENTA DE NUEVO.")
                    else:
                        break
                except ValueError:
                    print("INGRESA EL SEGUNDO NUMERO VALIDO")

            print(f"= {div1 / div2:.2f}")

        case 5:
            print("\n---- EXPONENTE ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    nume = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL PRIMER NUMERO VALIDO")

            print("^")

            while True:
                try:
                    exp = float(input(""))
                    break
                except ValueError:
                    print("INGRESA EL NUMERO DE EXPONENTE VALIDO")

            print(f"= {nume ** exp}")

        case 6:
            print("\n---- RAIZ CUADRADA ----")
            print("NOTA: *ESCRIBE EL NUMERO SEGUIDO DE ENTER")
            while True:
                try:
                    num = float(input("\u221a"))
                    if num < 0:
                        print("NO SE PUEDE CALCULAR RAIZ DE UN NUMERO NEGATIVO. INTENTA DE NUEVO.")
                    else:
                        break
                except ValueError:
                    print("INGRESA UN NUMERO VALIDO")

            print(f"= {num ** 0.5:.2f}")

        case 7:
            print("CERRANDO...")

        case _:
            print("\nSELECCIONA UNA OPCION VALIDA DEL MENU")


    if selec == 7:
        print("CIERRE DE SISTEMA EXITOSO.")
        break