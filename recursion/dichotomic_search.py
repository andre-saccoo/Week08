class DichotomicSearch():
    def __init__(self):
        pass

    def search(self, input,value):
        if len(input)==1:
            if input[0]==value:
                return True
            else:
                return False
        else:
            indice=len(input)//2
            return self.search(input[:indice],value) or self.search(input[indice:],value)


if __name__ == '__main__':
    sequenza = [1,2,3,4,5,6,7,8,9,10]
    dic=DichotomicSearch()
    print(dic.search(sequenza,11))