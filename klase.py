class Lista:

    def unos(self):
        lst = []
        k = int(input("Unesi broj "))
        while(k!=0):
            lst.append(k)
            k = int(input("Unesi broj "))
        return lst

    def sortiraj(self,lst):
        lst.sort(reverse=True)
        return lst

    def ispis(self,lst):
        print("Lista je: ", end="")
        for i in lst:
            print(i,end=" ")

    #ispis(sortiraj(unos()))

    '''lista = unos()
    lista = sortiraj(lista)
    ispis(lista)'''

