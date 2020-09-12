class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 2
            return 0
        else :
            Leftindex = 0
            Rightindex = 0
            checkL = 1
            checkR = 1
            for i in range(len(nums)):
                if self.findminIndex(nums[i],nums[i:]) and checkL :
                    Leftindex = i+1
                else : 
                    checkL = 0
                if self.findmaxIndex(nums[-i-1],nums[:-i-1]) and checkR :
                    Rightindex = -i-1
                else :
                    checkR = 0
                if checkL == 0 and checkR == 0:
                    return len(nums) + Rightindex - (Leftindex+1) + 1
            return 0
    def findminIndex(self,num,sublist):
        min = num
        for i in sublist:
            if i < min:
                min = i
        if min == num:
            return True
        else:
            return False
    def findmaxIndex(self,num,sublist):
        max = num
        for i in sublist:
            if i > max:
                max = i
        if max == num:
            return True
        else:
            return False
