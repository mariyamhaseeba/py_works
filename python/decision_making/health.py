tummy_size=int(input("enter the tummy size ="))
buttock_size=int(input("enter the buttock size ="))
gender=input("enter your gender : ")
measure=tummy_size/buttock_size
# if gender=="female" and  
# print(measure)
measure=round(measure,2)
# print(measure)
if (gender=="female"):
        if measure<=0.80:
         print("health risk is low ,body shape pear")
        
        elif measure<=0.85:
         print("health risk is moderate ,body shape is avocado")
        
        else:
         print("health risk is high , body shape is apple")
        
elif (gender=="male"):
        if measure<=0.95:
         print("health risk is low , body shape is pear")
        
        elif measure<=1.0:
         print("health risk is moderate , body shape is avocado")
        
        else:
         print("health risk is high , body shape is apple")
        
else:
 print("please enter the valid gender")
