a = input()  
if type(a):
   if a == "riha":
      address = input("enter the address")
      if address == "lalitpur" or address == "ktm": 
         print(a,address)


a = input()  
if type(a):
   if a == "riha" and address:
      address = input("enter the address")
      if address == "lalitpur" or address == "ktm": 
         print(a,address)










numbers = ['1',2,3,4,5]
for num in numbers:
   if num == '1': 
   
      print(num)
   else:
      print("other numbers",num)





for a in range(15):
   print("range",a)



count = 0
while count < 5:
   print(count)
   count += 2





x,y=10,20
y,x=y,x
print(x,y)


a = 5
b = 10
temp=a
b=temp


numbers=[1,2,3,4,5]
for num in numbers:
   if num==3:
      continue
   print("after continue",num)





   i=0
   while i<6:
      i+=1
      if i==3:
         break
      print(i)