import sys

# Arrieta Mancera Luis Sebastian 318174116
class Tablero:

    """
        Simula el tablero de un partido de tenis
    """
    
    class Jugador:
        
        """
            Simula los aspectos generales de un Jugador de Tenis
        """

        def __init__(self,nombre) -> None:
            self.nombre = nombre;
            self.puntaje = 0
            self.juegos = 0
            self.sets = 0
            self.adv = False #Ventaja
            
    def __init__(self,nombre_jugador1,nombre_jugador2) -> None:
        self.jugador1 = self.Jugador(nombre_jugador1)
        self.jugador2 = self.Jugador(nombre_jugador2)
        self.ganador = None
        self.juegos = 0
        self.set = 0
        self.resultados_set1 = {0: 0, 1:0 }
        self.resultados_set2 = {0: 0, 1:0 }
        self.resultados_set3 = {0: 0, 1:0 }
        self.puntos = {
                        0:0,
                        1:15,
                        2:30,
                        3:40,
                        4: "juego"}
        
    def generarPunto(self,jugador):

        """
            Metodo que le suma un punto al jugador pasado como parametro

            :param jugador: 0 para jugador1, 1 para el jugador2
        """

        # Jugador que gano el punto
        ganador_punto = None

        # Definimos el jugador que marco el punto 0: jugador1, 1: jugador2
        if jugador == 0:
            ganador_punto = self.jugador1
        else:
            ganador_punto = self.jugador2
        
        # Añadimos el punto
        ganador_punto.puntaje += 1

    def iguales(self):
        """
            Determina si los jugadores estan en 40-40 (Iguales)

            :return: True si estan en iguales False en caso contrario
        """
        return self.jugador1.puntaje == 3 and self.jugador2.puntaje == 3
    
    def tie_break(self):

        """
            Determina si el partido esta en Tie-Break!

            :return: True si estan en Tie-Break!, False en caso contrario
        """
        return self.jugador1.juegos == 6 and self.jugador2.juegos == 6

    def muestraPuntos(self,iguales = False, tie_break = False):

        """
            Imprime en terminal los puntos de los jugadores

            :param iguales: Si es True muestra los puntos con las ventajas de cada uno
            :param te_break: Si es True muestra los puntos del Tie-Break!
        """

        # Resultados del set 1
        rs1_j1 = self.resultados_set1.get(0) # Jugador 1
        rs1_j2 = self.resultados_set1.get(1) # Jugador 2

        # Resultados del set 2
        rs2_j1 = self.resultados_set2.get(0)
        rs2_j2 = self.resultados_set2.get(1)

        # Resultados del set 3
        rs3_j1 = self.resultados_set3.get(0)
        rs3_j2 = self.resultados_set3.get(1)

        # Puntajes
        puntaje_jugador1 = self.puntos.get(self.jugador1.puntaje)
        puntaje_jugador2 = self.puntos.get(self.jugador2.puntaje)

        if iguales:
            puntaje_jugador1 = "Adv" if self.jugador1.adv else 40
            puntaje_jugador2 = "Adv" if self.jugador2.adv else 40
        
        if tie_break:
            puntaje_jugador1 = self.jugador1.puntaje
            puntaje_jugador2 = self.jugador2.puntaje
            print("\tTIE-BREAK!\t")
            
        print(f" Jugador1 | {puntaje_jugador1} | \t| {rs1_j1} | {rs2_j1 if self.set > 0 else '-'} | {rs3_j1 if self.set > 1 else '-'} |")
        print(f" Jugador2 | {puntaje_jugador2} | \t| {rs1_j2} | {rs2_j2 if self.set > 0 else '-'} | {rs3_j2 if self.set > 1 else '-'} |")
    
    def reiniciaPuntos(self):
        """
            Reinicia los puntos de los jugadores a 0
        """
        self.jugador1.puntaje = 0
        self.jugador2.puntaje = 0

    def reiniciaJuegos(self):
        """
            Reinicia los juegos de los jugadores a 0
        """
        self.jugador1.juegos = 0
        self.jugador2.juegos = 0

    def reiniciaVentaja(self):
        """
            Reinicia la ventaja de los jugadores
        """
        self.jugador1.adv = False
        self.jugador2.adv = False

    def juego(self):

        """
            Simula un juego 
        """

        while self.ganador == None:
            menu = f"[0] {self.jugador1.nombre} (jugador1) \n[1] {self.jugador2.nombre} (jugador2)" 
            # Si estan en iguales
            if self.iguales():
                while True:
                    self.muestraPuntos(True)
                    print("\n")
                    print(menu)
                    j = int(input("Ingresa el jugador que anoto el punto: "))
                    # Si el punto lo anota el jugador 1
                    if j == 0:
                        # Verificamos si lleva la ventaja
                        if self.jugador1.adv:
                            # Jugador 1 gana la partida
                            self.ganador = self.jugador1
                            break
                        else:
                            # Si el jugador 2 lleva la ventaja
                            if self.jugador2.adv:
                                self.jugador2.adv = False
                            else:
                                self.jugador1.adv = True
                    else:
                        # Verificamos si lleva la ventaja
                        if self.jugador2.adv:
                            # Jugador2 gana la partida
                            self.ganador = self.jugador2
                            break
                        else:
                            # Si el jugador 1 lleva la ventaja
                            if self.jugador1.adv:
                                self.jugador1.adv = False
                            else:
                                self.jugador2.adv = True
            else:
                self.muestraPuntos()
                print("\n")
                print(menu)
                j = int(input("Ingresa el jugador que anoto el punto: "))
                self.generarPunto(j)

                if self.jugador1.puntaje == 4:
                    # Jugador 1 gana el juego
                    self.ganador = self.jugador1
                
                if self.jugador2.puntaje == 4:
                    # Jugador 2 gana el juego
                    self.ganador = self.jugador2

        self.ganador.juegos += 1

        # Vamos guardando un registro de los juegos ganados
        if self.set == 0:
            self.resultados_set1[0] = self.jugador1.juegos
            self.resultados_set1[1] = self.jugador2.juegos
        if self.set == 1:
            self.resultados_set2[0] = self.jugador1.juegos
            self.resultados_set2[1] = self.jugador2.juegos
        if self.set == 2:
            self.resultados_set3[0] = self.jugador1.juegos
            self.resultados_set3[1] = self.jugador2.juegos

        self.reiniciaVentaja()
        self.reiniciaPuntos()

        # Avisamos que el juego termino
        print(f"JUEGO TERMINADO el jugador {self.ganador.nombre} se lleva el juego")
  
    def sett(self):

        """
            Simula jugar por set      
        """
        ganador_set = None

        while ganador_set == None:

            self.juego()

            # Avisamos el cambio de cancha
            if  ((self.jugador1.juegos + self.jugador2.juegos) % 2) == 1:
                print("CAMBIO DE CANCHA!")

            self.ganador = None

            # Verificar si llegamos a un Tie-Break!
            if self.tie_break():
                # Ganador del Tie-Break!
                ganador_tie_break = None

                # Reiniciamos los puntos para el Tie-Break!
                self.reiniciaPuntos()

                while ganador_tie_break == None:

                    # Verificamos si algun jugador llego a 7 con diferencia de 2
                    if self.jugador1.puntaje >= 7 and self.jugador1.puntaje >= self.jugador2.puntaje + 2:
                        # Jugador 1 se lleva el set
                        ganador_tie_break = self.jugador1
                        break
                    
                    if self.jugador2.puntaje >= 7 and self.jugador2.puntaje >= self.jugador1.puntaje + 2:
                        # Jugador 2 se lleva el set
                        ganador_tie_break = self.jugador2
                        break

                    # Mostramos el tablero con Tie-Break
                    self.muestraPuntos(False,True)
                    print("\n")
                    # Menu
                    menu = f"[0] {self.jugador1.nombre} (jugador1) \n[1] {self.jugador2.nombre} (jugador2)" 
                    print(menu)
                    j = int(input("Ingresa el jugador que anoto el punto: "))
                    # Marcamos el punto
                    self.generarPunto(j)

                # Ganador del set
                ganador_set = ganador_tie_break
                ganador_set.juegos += 1

                # Vamos guardando un registro de los juegos ganados
                if self.set == 0:
                    self.resultados_set1[0] = self.jugador1.juegos
                    self.resultados_set1[1] = self.jugador2.juegos
                if self.set == 1:
                    self.resultados_set2[0] = self.jugador1.juegos
                    self.resultados_set2[1] = self.jugador2.juegos
                if self.set == 2:
                    self.resultados_set3[0] = self.jugador1.juegos
                    self.resultados_set3[1] = self.jugador2.juegos

            else:
                # Verificamos si alguno de los jugadores llego a 6 juegos con diferencia de 2 juego
                if self.jugador1.juegos >= 6 and self.jugador1.juegos >= self.jugador2.juegos + 2:
                    # Jugador 1 se lleva el set
                    ganador_set = self.jugador1
                
                # Verificamos si alguno de los jugadores llego a 6 juegos con diferencia de 2 juegos
                if self.jugador2.juegos >= 6 and self.jugador2.juegos >= self.jugador1.juegos + 2:
                    # Jugador 2 se lleva el set
                    ganador_set = self.jugador2

        ganador_set.sets += 1

        # Indicamos que jugamos un set
        self.set += 1

        # Reiniciamos los puntos una vez terminado el set
        self.reiniciaPuntos()

        # Reiniciamos los juegos una vez terminado el set
        self.reiniciaJuegos()

        # Indicamos el jugador que gano el set
        print(f"SET TERMINADO el jugador {ganador_set.nombre} se lleva el set")

    def partido(self):

        """
            Simula jugar un partido
        """
        self.ganador = None

        self.preprocesamiento(0,4,4)
        # Registramos set 1
        self.sett()
        self.preprocesamiento(1,4,4)
        # Registramos set 2
        self.sett()
        # Verificamos si algun jugador ha ganado dos sets
        if self.jugador1.sets == 2:
            self.ganador = self.jugador1
        elif self.jugador2.sets == 2:
            self.ganador = self.jugador2
        else:
            self.preprocesamiento(2,4,4)
            # Registramos set 3
            self.sett()
            self.ganador = self.jugador1 if self.jugador1.sets == 2 else self.jugador2

        # Mostramos el resultado final
        print("\nPARTIDO TERMINADO (Resultados finales)")
        self.muestraPuntos()
        print(f"\n EL GANADOR ES: {self.ganador.nombre}")

    def preprocesamiento(self,set,juegos_jugador1,juegos_jugador2):

        """
            Realiza un preprocesamiento para modificar los juegos de los jugadores

            :param set: el set para el cual se esta modificando los juegos
            :param juegos_jugador1: juegos ganados del jugador 1
            :param juegos_jugador2: juegos ganados del jugador 2

        """
        self.jugador1.juegos = juegos_jugador1
        self.jugador2.juegos = juegos_jugador2

        if self.set == 0:
            self.resultados_set1[0] = self.jugador1.juegos
            self.resultados_set1[1] = self.jugador2.juegos

        if self.set == 1:
            self.resultados_set2[0] = self.jugador1.juegos
            self.resultados_set2[1] = self.jugador2.juegos
        
        if self.set == 2:
            self.resultados_set3[0] = self.jugador1.juegos
            self.resultados_set3[1] = self.jugador2.juegos

if __name__ == "__main__":

    # Recibimos los nombres de los jugadores por terminal
    if len(sys.argv) == 3:
        # Creamos un tablero con los nombres de los jugadores
        t = Tablero(sys.argv[1],sys.argv[2])
        # Jugamos un partido
        t.partido()
    else:
        print("Error: No se proporcionaron los argumentos exactos, por favor al momento de ejecutar el programa agrega los nombres de los dos jugadores separados por espacio")
        

        
        


            

        

    
        


