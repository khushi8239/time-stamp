import time
a = int(input("enter the time"))
print("enter the time",a)
if(a<9):
   timestamp = time.strftime('%H')
   print(timestamp)
   timestamp = time.strftime('%M')
   print(timestamp)
   timesstamp = time.strftime('%S')
   print(timestamp)
   print("good morning")
elif(a<16):
   timestamp = time.strftime('%H')
   print(timestamp)
   timestamp = time.strftime('%M')
   print(timestamp)
   timesstamp = time.strftime('%S')
   print(timestamp)
   print("good evening")
else:
   timestamp = time.strftime('%H')
   print(timestamp)
   timestamp = time.strftime('%M')
   print(timestamp)
   timesstamp = time.strftime('%S')
   print(timestamp)
   print("good night")
    
 


