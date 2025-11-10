from database.DAO import DAO

class Model:
    def __init__(self):
        pass


    def calcola_anagrammi(self, parola):
        self._anagrammi=[]
        self.ricorsione("", parola) # anagramma_parziale, lettere rimanenti, la prima volta che la chiamo è tutte le lettere della parola
        return self._anagrammi


    def ricorsione(self, anagramma_parziale,lettere_rimanenti):
        if len (lettere_rimanenti) == 0:
            self._anagrammi.append(anagramma_parziale)
            return
        else:
            for i in range (len(lettere_rimanenti)):
                anagramma_parziale+=lettere_rimanenti[i]
                nuove_lettere_rimanenti=lettere_rimanenti[:i]+lettere_rimanenti[i+1:]
                self.ricorsione(anagramma_parziale,nuove_lettere_rimanenti)
                anagramma_parziale=anagramma_parziale[:-1]

if __name__ == '__main__':
    model = Model()
    print(model.calcola_anagrammi("DOG"))