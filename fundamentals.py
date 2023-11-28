x = -50
name = "Opeyemi"
employed = True
print(x)
print(name)
print(employed)
if (x > 10):
    print('That is larger than 10') 
else: 
    print ('That is not larger than 10')

if((x < 0) and employed == True):
    print("Negative and True")

if((x > 0) and employed == False):
    print("Positive and False")

if((x > 100) or employed == True):
    print("Large or True")

else:
    print("I dont know")
