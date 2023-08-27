import sys

class Tablero:

    class Jugador:
        
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
        self.set = 1
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

        # Jugador que gano el punto
        ganador_punto = None

        # Definimos el jugador que marco el punto 0: jugador1, 1: jugador2
        if jugador == 0:
            ganador_punto = self.jugador1
        else:
            ganador_punto = self.jugador2
        
        # Añadimos el punto
        ganador_punto.puntaje+=1

    def iguales(self):
        return self.jugador1.puntaje == 3 and self.jugador2.puntaje == 3
    
    def tie_break(self):
        return self.jugador1.juegos == 6 and self.jugador2.juegos == 6

    def muestraPuntos(self,iguales = False):

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
            
        print(f" Jugador1 | {puntaje_jugador1} | \t| {rs1_j1} | {rs2_j1 if self.set > 1 else '-'} | {rs3_j1 if self.set > 2 else '-'} |")
        print(f" Jugador2 | {puntaje_jugador2} | \t| {rs1_j2} | {rs2_j2 if self.set > 1 else '-'} | {rs3_j2 if self.set > 2 else '-'} |")
    
    def reiniciaPuntos(self):
        self.jugador1.puntaje = 0
        self.jugador2.puntaje = 0

    def reiniciaVentaja(self):
        self.jugador1.adv = False
        self.jugador2.adv = False

    def partida(self):
        while self.ganador == None:
            menu = f"[0] {self.jugador1.nombre} (jugador1) \n[1] {self.jugador2.nombre} (jugador2)" 
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
        self.resultados_set1[0] = self.jugador1.juegos
        self.resultados_set1[1] = self.jugador2.juegos
        self.reiniciaVentaja()
        self.reiniciaPuntos()

    def main(self):
        
        ganador_set = None

        while ganador_set == None:
            self.partida()
            self.ganador = None

            # Verificar si llegamos a un Tie-Break!
            if self.tie_break():
                # Ganador del Tie-Break!
                ganador_tie_break = None

                # Reiniciamos los puntos de los jugadores
                self.reiniciaPuntos()

                while ganador_tie_break == None:
                     
                     # Mostramos el tablero
                     
                     # Menu
                     menu = f"[0] {self.jugador1.nombre} (jugador1) \n[1] {self.jugador2.nombre} (jugador2)" 
                     j = int(input("Ingresa el jugador que anoto el punto: "))
                     
                

            else:
                # Verificamos si alguno de los jugadores llego a 6 juegos con diferencia de 2 juego
                if self.jugador1.juegos >= 6 and self.jugador1.juegos == self.jugador2.juegos + 2:
                    # Jugador 1 se lleva el set
                    ganador_set = self.jugador1
                
                # Verificamos si alguno de los jugadores llego a 6 juegos con diferencia de 2 juegos
                if self.jugador2.juegos >= 6 and self.jugador2.juegos == self.jugador1.juegos + 2:
                    # Jugador 2 se lleva el set
                    ganador_set = self.jugador2

        ganador_set.sets += 1

                

t = Tablero("","")
t.main()
        
        


            

        

    
        


