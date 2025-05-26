class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List():
    def __init__(self):
        self.head = Node()

    def append(self,data):
        appended_node = Node(data)
        if self.head.data == None:
            self.head = appended_node
        else:
            counter = self.head
            while counter.next != None:
                counter = counter.next
            counter.next = appended_node

    def display(self):
        counter = self.head
        print(counter.data)
        while counter.next != None:
            print(counter.next.data)
            counter = counter.next
    def length(self):
        counter = self.head
        if self.head.data == None:
            return 0
        output = 1
        while counter.next != None:
            counter = counter.next
            output +=1
        return output
    def drop(self, i):
        if self.head.data == None:
            print('lista jest pusta')
            return
        if i>= self.length() or i<0:
            print('zly indeks')
            return
        if i == 0:
            self.head = self.head.next
            return
        counter = self.head
        position = 0
        while counter.next != None:
            former = counter
            counter = counter.next
            if position+1 == i:
                former.next = counter.next
                return
            position += 1


    def reverse_iter(self): 
        former = None
        counter = self.head
        while counter: 
            consequent = counter.next
            counter.next = former 
            former = counter 
            counter = consequent 
        self.head = former 

    def reverse_recur(self): 
        def reverse_recur_inner(counter, former): 
            if not counter: 
                self.head = former
                return

            consequent = counter.next
            counter.next = former 
            reverse_recur_inner(consequent, counter)
        reverse_recur_inner(counter=self.head, former= None)

lista = List()
lista.append(3)
lista.append(3)
lista.append(10)
lista.append(7)
lista.append(5)


print('Lista przed odwroceniem:')
lista.display()
lista.reverse_iter()
print('Lista po odwroceniu iteracyjnym:')
lista.display()   

lista.reverse_recur()
print('Lista po odwroceniu rekurencyjnym:')
lista.display()

 