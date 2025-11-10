from functools import lru_cache
from time import time

'''
ci costruiamo una struttura dati per memorizzare i dati intermedi,se il dato è già presente non calcolo, se non c'è lo calcolo e lo aggiungo
stesso valore differenti tempi
senza caching
63245986
1.1920928955078125e-05
con caching
63245986
1.0013580322265625e-05
'''

class Fibonacci:
    def __init__(self):
        self._cache={0:0,1:1}

    @lru_cache(maxsize=None)
    def calcola_elemento(self,n: int):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return (self.calcola_elemento(n-1)+self.calcola_elemento(n-2))

    def calcola_elemento_caching(self,n: int):
        # DOVE METTO LA CACHE? tra le variabili di classe
        if self._cache.get(n) is not None:
            return self._cache[n]
        else:
            self._cache[n] = self.calcola_elemento_caching(n-1)+self.calcola_elemento_caching(n-2)
            return self._cache[n]

if __name__ == '__main__':
    fibonacci = Fibonacci() #controlliamo se è importato o eseguito direttamente
    print("senza caching, ma con decoratore")
    start_time=time()
    print(fibonacci.calcola_elemento(39))
    end_time = time()
    print(end_time - start_time)
    fibonacci = Fibonacci()  # controlliamo se è importato o eseguito direttamente

    print("con caching")
    start_time = time()
    print(fibonacci.calcola_elemento_caching(39))
    end_time = time()
    print(end_time - start_time)


