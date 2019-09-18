from sys import stdin

class Nodo:
    
    def __init__(self,key):
        self.key = key
        self.next = None

class Fila:
    
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def queu(self,nombre):

        new=Nodo(nombre)

        if self.length == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self.length += 1

    def dequeu(self):

        if self.length == 0:
            print("No hay fila")

        else:
            print(self.head.key)
            self.head = self.head.next
            self.length -= 1
            
def main():
    x=int(stdin.readline().strip())
    for i in range(x):
        line=int(stdin.readline().strip())
        fila=Fila()
        
        for j in range(line):
            nombre=stdin.readline().strip()
            if nombre=="Siguiente":
                fila.dequeu()
            else:
                fila.queu(nombre)

main()
