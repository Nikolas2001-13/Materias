from sys import stdin

class Nodo:

    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None

class Mano:

    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def mazo(self,card):

        new = Nodo(card)
        
        if  self.length == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self.length += 1
            
    
    def quitar(self):
        
        if self.length == 0:
            return None

        elif self.head == self.tail:
            return self.head

        else:
            now = self.head.next
            card = self.head
            self.head = now
            self.length -= 1
            return card      
        
def main():
    n=int(stdin.readline().strip())
    while n!=0:
        mano=Mano()
        discarded = ""
        
        for i in range(1,n+1):
            mano.mazo(str(i))
            
        while mano.head.key != mano.tail.key:
            discarded += mano.quitar().key + ", "
            mano.mazo(mano.quitar().key)
            
        print("Discarded cards:",discarded[:-2])
        print("Remaining card:",mano.head.key)
        
        n=int(stdin.readline().strip())

main()

        
