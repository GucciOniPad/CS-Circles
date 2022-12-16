#The function takes an pos int n and adds the digits together 
#This process is repeated until there is a single digit number
def digitalSum(n):
  def realSum(n): 
         nonlocal result 
         whole = n//10
         rest = n % 10
         if whole < 10: result = whole
         else: realSum(whole)
         result += rest 
  if n < 10: return n
  result = 0
  realSum(n)
  return result

def digitalRoot(n): 
    if len(str(n)) == 1: return n
    n = digitalSum(n)
    return digitalRoot(n)
print(digitalRoot(2019))