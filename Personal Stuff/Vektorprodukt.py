a = input("Enter coordinates, seperated with commas (a1, a2, a3):")
#b = input("Enter coordinates, seperated with commas (b1, b2, b3):") 
a = a.replace(",", " |")
#b = b.replace(",", " |")
a = a.replace(" ", "")

a1 = ""
a2 = ""
a3 = ""
pos = int(0)


for i in range(0, len(a)): 
    if a[i] == "|": 
        a1 = a[pos:i]
        pos = i 

print(1)