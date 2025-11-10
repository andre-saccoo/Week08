class QuickSort():
    def __init__(self):
        pass
    def sort(self):
        if len(sequenza)<=1: #se lunghezza 0 o 1 non ha senso proseguire
            return sequenza
        else:
            #1) scegliere il pivot
            pivot=sequenza[0]
            #2) dividere la sequenza in sottosequenza
            sequenza_minori=[]
            for i in range(1, len(sequenza)):
                if sequenza[i]<pivot:
                    sequenza_minori.append(sequenza[i])
                sequenza_uguali=[n for n in sequenza == pivot]
                sequenza_maggiori=[n for n in sequenza if n>pivot]
            # 3) fare il sort delle sottosequenza e appendere i risultati
        return self.sort(sequenza_minori)+sequenza_uguali+self.sort(sequenza_maggiori)

if __name__ == '__main__':
    sequenza=[3,7,11, 2,5,9,4,7]
    qs=QuickSort()
    print(qs.sort(sequenza))