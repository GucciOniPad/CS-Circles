def nestedListSum(NL):
    if isinstance(NL, int):    
        return NL              
    sum = 0                     
    for i in range(0, len(NL)): 
        sum = sum + nestedListSum(NL[i])
    return sum

def nestedListContains(NL, target):
    if isinstance(NL, int) and NL == target: return True # case1: only one int item as input and equal to target
    elif isinstance(NL, int) and NL != target: return False # case2: only one int item as input but unequal to target
    
    for i in range(0, len(NL)): 
         if NL[i] == target: return True 
         else: nestedListContains(NL[i], target)
    return False

# current status: the code is working for lists. The problem we have now is to get it running for lists inside of other lists...

# Test section
print(nestedListContains([1, [9, 2], 3], 3))
# print(nestedListSum([3]))

#var = [1, 2, 3, 4]
# print(isinstance(var, int)) # Is instance is only used for single numbers 