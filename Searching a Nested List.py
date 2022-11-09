def nestedListSum(NL):
    if isinstance(NL, int):    
        return NL              
    sum = 0                     
    for i in range(0, len(NL)): 
        sum = sum + nestedListSum(NL[i])
    return sum

def nestedListContains(NL, target):
    if isinstance(NL, int) and NL == target: return True # case1: only one int item as input and equal to target
    if isinstance(NL, int) and NL != target: return False # case2: only one int item as input but unequal to target
    
    for i in range(0, len(NL)): 
        containsTarget = nestedListContains(NL[i], target)
        if containsTarget: 
            return True
    return False


# Test section
print(nestedListContains([1, 2, 3, [4, 5, 2, [8]]], 8))
# print(nestedListSum([3]))

#var = [1, 2, 3, 4]
# print(isinstance(var, int)) # Is instance is only used for single numbers 