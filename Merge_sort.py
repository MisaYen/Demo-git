class Merge_sort():
    def sort(self,nlst):
        if len(nlst) == 1:
            return nlst
        mid = len(nlst) //2
        left = nlst[:mid]
        right = nlst[mid:]
        left = self.sort(left)
        right = self.sort(right)
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        output = []
        while left and right:
            if left[0] < right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        
        if left:
            output += left
        if right:
            output += right
            
        return output
        
'''
num = eval(input("ENter a list: "))
print(Merge_sort().sort(num))        '''