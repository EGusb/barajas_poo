'''
Vamos a hacer una baraja de cartas españolas orientado a objetos.
Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)
La baraja estará compuesta por un conjunto de cartas, 40 exactamente.
Las operaciones que podrá realizar la baraja son:

- barajar: cambia de posición todas las cartas aleatoriamente
- siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final,
                  se indica al usuario que no hay más cartas.
- cartasDisponibles: indica el número de cartas que aún puede repartir
- darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver).
            En caso de que haya menos cartas que las pedidas, no devolveremos nada pero debemos indicárselo al usuario.
- cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario
- mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método,
                 este no mostrara esa primera carta.
'''
from ej_poo_silver_barajas_clases import Baraja

print()
print("¡Bienvenido/a a Croupier Mágico! Vamos a repartir algunas cartas...")
baraja = Baraja()
baraja.setear_baraja()

while True:
    print()
    print("Elija una de las siguientes opciones:")
    menu = baraja.mostrar_menu()
    for i in menu:
        print(f"({i})  {menu[i]}")
    print("(-1)  Guardar la baraja (cerrar programa)")

    try:
        opcion = int(input("  --->  "))
        if opcion in menu:
            print(f"Se ha elegido la opción {opcion}: {menu[opcion]}")
            
            '''
            1: "Mezclar el la baraja",
            2: "Sacar una carta de la baraja",
            3: "Mostrar la cantidad de cartas que quedan en la baraja",
            4: "Sacar varias cartas de la baraja",
            5: "Mostrar las cartas que ya han salido de la baraja y están en el montón",
            6: "Mostrar las cartas que aún siguen en la baraja",
            7: "Generar de nuevo la baraja"
            '''
            if opcion == 1:
                veces = int(input("¿Cuántas veces quiere mezclar la baraja?  --->  "))
                baraja.barajar(veces)
            
            if opcion == 2:
                baraja.siguiente_carta()
            
            if opcion == 3:
                baraja.cartas_disponibles()
            
            if opcion == 4:
                cantidad = int(input("¿Cuántas cartas quiere sacar de la baraja?  --->  "))
                baraja.dar_cartas(cantidad)
            
            if opcion == 5:
                baraja.cartas_monton()
            
            if opcion == 6:
                baraja.mostrar_baraja()

            elif opcion == 7:
                baraja.setear_baraja()

        elif opcion == -1:
            print("CERRANDO PROGRAMA...")
            print()
            break
        
        else:
            raise Exception("¡OPCIÓN INVÁLIDA!")

    except Exception as e:
        print(f"¡HA OCURRIDO UN ERROR!   --->   {type(e).__name__}:  {e}")