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
# https://python-para-impacientes.blogspot.com/2015/09/el-modulo-random.html
import random

class Baraja():
    '''Clase que representa un conjunto de 40 cartas españolas, con números del 1 al 12 (sin 8s y 9s)'''
    def __init__(self):
        '''Constructor de la clase Baraja'''
        self.en_baraja = []     # Lista que contiene las cartas que están aún en la baraja, sin salir
        self.en_monton = []     # Lista que contiene las cartas que ya han salido de la baraja
        self.__palos = ["espadas", "bastos", "oros", "copas"]
        self.__numeros = ["1","2","3","4","5","6","7","10","11","12"]

    def setear_baraja(self):
        '''Método que genera una baraja con 40 cartas españolas. Envía todas las cartas del montón a la baraja.
        La nueva baraja está ordenada de menor a mayor, y por palo: espadas, bastos, oros y copas'''
        self.en_baraja = []
        self.en_monton = []
        for palo in self.__palos:
            for num in self.__numeros:
                carta_nueva = Carta(palo, num)
                self.en_baraja.append(carta_nueva)
        print("¡Se ha creado una baraja de 40 cartas!")
    
    def barajar(self, veces=1):
        '''Método que mezcla las cartas que aún están en la baraja, tantas veces como se indique. Por defecto, se baraja una sola vez'''
        for i in range(0, veces):
            random.shuffle(self.en_baraja)
        if veces == 1:
            print(f"La baraja ha sido mezclada {veces} vez")
        else:
            print(f"La baraja ha sido mezclada {veces} veces")
    
    def dar_cartas(self, cantidad):
        '''Método que devuelve tantas cartas como se pidan, y las envía al mazo del montón. 
        Si no hay tantas cartas en la baraja como se piden, no se devuelve ninguna y se devuelve un mensaje.'''
        if cantidad <= len(self.en_baraja):
            for i in range(0, cantidad):
                carta_sacada = self.en_baraja.pop(0)
                self.en_monton.append(carta_sacada)
                print(f"Se sacó la carta:  {carta_sacada}")
        else:
            print("No hay tantas cartas en la baraja.")

        if len(self.en_baraja) == 0:
            print("¡NO QUEDAN MÁS CARTAS EN LA BARAJA!")

    def siguiente_carta(self):
        '''Devuelve la siguiente carta en la baraja y la coloca en el montón.'''
        self.dar_cartas(1)
    
    def cartas_disponibles(self):
        '''Muestra el número de cartas que aún quedan en la baraja sin repartir.'''
        print(f"Quedan {len(self.en_baraja)} cartas en la baraja")
    
    def cartas_monton(self):
        '''Muestra las cartas que han salido de la baraja y se encuentran en el montón.'''
        if len(self.en_monton) > 0:
            for i in self.en_monton:
                print(i)
        else:
            print("No hay cartas en el montón.")
    
    def mostrar_baraja(self):
        '''Muestra las cartas que aún quedan en la baraja.'''
        if len(self.en_baraja) > 0:
            print("Se muestran las cartas que quedan en la baraja:")
            for i in self.en_baraja:
                print(i)
        else:
            print("No hay cartas en la baraja.")
    
    def mostrar_menu(self):
        '''Método que devuelve un diccionario con las opciones disponibles para la baraja.'''
        menu = {
        1: "Mezclar el la baraja",
        2: "Sacar una carta de la baraja",
        3: "Mostrar la cantidad de cartas que quedan en la baraja",
        4: "Sacar varias cartas de la baraja",
        5: "Mostrar las cartas que ya han salido de la baraja y están en el montón",
        6: "Mostrar las cartas que aún siguen en la baraja",
        7: "Generar de nuevo la baraja"}
        return menu

class Carta():
    '''Clase que representa una carta española, con número y palo'''
    def __init__(self, palo, numero):
        '''Constructor de la clase Carta'''
        self.palo = palo
        self.numero = numero
    
    def __str__(self):
        return f"{self.numero} de {self.palo}"