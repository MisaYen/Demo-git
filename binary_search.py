class binary_search():
    def search(self,nlst,key):
        Low = 0
        Hight = len(nlst)-1
        middle = int((Hight + Low)/2)
        times = 0
        while True:
            times += 1
            if key == nlst[middle]:
                rtn = middle
                break
            elif key < nlst[middle]:
                Hight = middle-1
                middle = int((Hight + Low)/2)
            else :
                Low = middle +1
                middle = int((Hight + Low)/2)
            if Low > Hight:
                rtn = -1
                break
        return rtn , times
    
data = [19,32,28,99,10,88,62,8,6,3]
sorted_data = sorted(data)
key = int(input("Inter Key: "))
print(binary_search().search(sorted_data,key))
