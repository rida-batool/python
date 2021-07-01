
def singleNumber(self, nums: List[int]) -> int:
    myDict = {}
    for number in nums:
        if (number not in myDict):
            myDict[number] = 1
        elif (number in myDict):
            myDict[number] = myDict[number]+1
    print(myDict)        
        
    print(list(myDict.keys())[list(myDict.values()).index(1)])
    return (list(myDict.keys())[list(myDict.values()).index(1)])

singleNumber([2,2,1]) 