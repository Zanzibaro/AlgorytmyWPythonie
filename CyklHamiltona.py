class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 
        self.V = vertices 


    def isSafe(self, v, pos, path): 

        if self.graph[ path[pos-1] ][v] == 0: 
            return False

        for vertex in path: 
            if vertex == v: 
                return False

        return True

    def hamCycleUtil(self, path, pos): 

        if pos == self.V: 

            if self.graph[ path[pos-1] ][ path[0] ] == 1: 
                return True
            else: 
                return False

        for v in range(1,self.V): 

            if self.isSafe(v, pos, path) == True: 

                path[pos] = v 

                if self.hamCycleUtil(path, pos+1) == True: 
                    return True

                path[pos] = -1

        return False

    def hamCycle(self): 
        path = [-1] * self.V 

        path[0] = 0

        if self.hamCycleUtil(path,1) == False: 
            print ("Rozwizanie nie istnieje\n")
            return False

        self.printSolution(path) 
        return True

    def printSolution(self, path): 
        print ("Rozwiazanie istnieje: Oto",
                 "cykl Hamiltona")
        for vertex in path: 
           print (vertex )


# Driver Code 

''' Tworzymy nastepujacy graf
    (0)--(1)--(2) 
    | / \ | 
    | / \ | 
    | /     \ | 
    (3)-------(4) '''
g1 = Graph(5) 
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1], 
            [0, 1, 1, 1, 0], ] 

# Wydrukuj rozwiazanie 
g1.hamCycle(); 

''' Tworzymy nastepujacy graf 
    (0)--(1)--(2) 
    | / \ | 
    | / \ | 
    | /     \ | 
    (3)     (4) '''
g2 = Graph(5) 
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0], 
        [0, 1, 1, 0, 0], ] 

# Wydrukuj rozwiazanie
g2.hamCycle();