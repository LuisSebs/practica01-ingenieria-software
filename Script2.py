def exist(arr, b):

    """
        Dado un arreglo y un numero objetivo encontrar dos números
        distintos dentro del arreglo tal que su suma
        sea igual al numero objetivo

        Nota: La complejidad de este algoritmo es O(n)
        ya que para un arreglo de n entradas solo basta
        con recorrer una vez todo el arreglo.

        :param arr: arreglo de numeros
        :param b: numero objetivo
        :return: True si existen dos numero, False en caso contrario

    """

    # Numeros encontrados
    encontrados = set()

    # Recorremos todo el arreglo
    for a in arr:
        # Ecuacion que representa este problema
        # a + x = b --> x = b - a, con a y b constantes
        x = b - a
        # Verificamos si el numero que lo complementa esta en los numeros que hemos encontrado y ambos numeros no son iguales
        if (x in encontrados) and x != a:
            # Regresamos los numeros que sumados dan como resultado target
            return [x, a]
        else:
            encontrados.add(a)    
    return []

class BinaryTree():

    def __init__(self) -> None:
        self.root = None
    
    def insert(self,node, next = None):

        # Si queremos insertar a partir de un nodo
        if next:
            # Si el valor a insertar es mayor o igual
            if node.value >= next.value:
                # Lo ponemos en el lado derecho
                if next.right == None:
                    next.right = node
                else:
                    # Llamada recursiva
                    self.insert(node=node,next=next.right)
            # Si el valor a insertar es menor
            else:
                # Lo ponemos en el lado izquierdo
                if next.left == None:
                    next.left = node
                else:
                    # Llamada recursiva
                    self.insert(node=node,next=next.left)  
        # En caso contrario insertamos desde la raiz
        else:
            # Si la raiz es vacia
            if self.root == None:
                self.root = node
            # Llamada recursiva
            else:
                self.insert(node=node,next=self.root)

    def preorden(self,node = None, l = None):

        """
            Recorrido de un arbol en preorden (raiz, izquierda, derecha)

            :param node: nodo a partir del cual queremos realizar preorden
        """

        if node:
            # Raiz
            l.append(node.value)
            # Izquierda
            if node.left != None:
                self.preorden(node=node.left,l=l)
            # Derecha
            if node.right != None:
                self.preorden(node=node.right,l=l)
            
            return l
        else:
            return self.preorden(self.root,[])
        
    def inorden(self,node = None, l = None):

        """
            Recorrido de un arbol en inorden (izquierda,raiz,derecha)

            :param node: nodo a partir del cual queremos realizar preorden
        """

        if node:
            # Izquierda
            if node.left != None:
                self.inorden(node=node.left,l=l)
            # Raiz
            l.append(node.value)
            # Derecha
            if node.right != None:
                self.inorden(node=node.right,l=l)
            
            return l
        else:
            return self.inorden(self.root,[])
    
    def postorden(self,node = None, l = None):

        """
            Recorrido de un arbol en postorden (izquierda, derecha, raiz)

            :param node: nodo a partir del cual queremos realizar preorden
        """

        if node:
            # Izquierda
            if node.left != None:
                self.postorden(node=node.left,l=l)
            # Derecha
            if node.right != None:
                self.postorden(node=node.right,l=l)
            # Raiz
            l.append(node.value)
            return l
        else:
            return self.postorden(self.root,[])

    class Node():
        
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

def menuExist():
    k = None
    arr = []
    while True:
        print(f"[0] Agrega elementos a la lista {'' if len(arr) == 0 else arr} \n[1] Agregar K {'' if k == None else '(k = '+str(k)+')'} \n[2] Correr metodo \n[3] Regresar")
        op1 = int(input("Elige una opcion: "))
        if op1 == 0:
            nums = input("Ingresa los numeros separados por espacio: ")
            for n in nums.split(' '):
                arr.append(int(n))
        elif op1 == 1:
            k = int(input("Ingresa un numero: "))
        elif op1 == 2:
            if k != None and len(arr) != 0:
                print(exist(arr,k))
            else:
                print("Por favor ingresa k y llena el arreglo de elementos")
        elif op1 == 3:
            print("\n")
            break
        else:
            print("Opcion no valida")
        print("\n")

def makeTree():
    
    t = BinaryTree()

    while True:

        menu = "[0] insertar nodo \n[1] preorden \n[2] inorden \n[3] postorden \n[4] Regresar"
        print(menu)
        op = int(input("Ingresa una opcion: "))
        print("\n")
        
        # Agregar elemento
        if op == 0:
            v = int(input("Ingresa un valor a insertar al arbol: "))
            n = t.Node(v)
            t.insert(n)
        # Recorrido en preorden
        elif op == 1:
            if t.root != None:
                print(t.preorden([]))
            else:
                print("Por favor llena el arbol antes")
        # Recorrido en inorden
        elif op == 2:
            if t.root != None:
                print(t.inorden([]))
            else:
                print("Por favor llena el arbol antes")
        # Recorrido en postorden
        elif op == 3:
            if t.root != None:
                print(t.postorden([]))
            else:
                print("Por favor llena el arbol antes")
        # Salir de la funcion
        elif op == 4:
            print("\n")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":

    while True:
        print("[0] Existe s_i,s_j con i!=j talque s_i + s_j = k \n[1] Crear arbol \n[2] Salir del programa")
        op = int(input("Ingresa una opcion: "))
        print("\n")
        if op == 0:
            menuExist()
        elif op == 1:
            makeTree()
        elif op == 2:
            break
        else:
            print("Opcion invalida")
                    



        

            
        
            
