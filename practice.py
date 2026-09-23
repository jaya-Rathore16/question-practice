#type casting
'''
a=10
print(type(a))
print(complex(a))
'''


#calcluate SI value
'''
aum=int(input("Enter Principle Amount"))
rate=int(input("Enter the rate of intrest per anum"))
time=int(input("Enter The Time in year"))
print((aum*rate*time)/100,"is your SI")
'''
#compairing thre number usig nexted load
'''
a=int(input("enter the number "))
b=int(input("enter the number "))
c=int(input("enter the number "))
if(a<b):
  if(a<c):
     print("a is smallest")
  elif(a==c):
     print("a and c are equal")
  else:
     print("c is the smallest")

elif(b<c):
   if(b<a):
     print("b is smallest" )
   elif(b==a):
      print("a and b are equle")

elif(c<b):
   if(c<a):
    print("c is the smallest")
   elif(c==a):
      print("c and a are equal")

elif(a==b):
   if(b==c):
      print("all are equal")
else:
   print("b and c are equal")
'''