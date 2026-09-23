#type casting
'''
a=10
print(type(a))
print(complex(a))

#calcluate SI value
aum=int(input("Enter Principle Amount"))
rate=int(input("Enter the rate of intrest per anum"))
time=int(input("Enter The Time in year"))
print((aum*rate*time)/100,"is your SI")


#compairing thre number usig nexted load
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
'''
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3: 
        print("num1 is greater than num2 and num3")
    elif num3 > num1:
        print("Num3 is greater than num1 and num2")
    else:
        print("num1 and Num3 are equal")
elif num2 > num1:
    if num2 > num3:
        print("num2 is greater than num1 and num3")
    elif num3 > num2:
        print("Num3 is greater than num1 and num2")
    else:
        print("num2 and Num3 are equal")
elif num1 == num2:
    if num1 > num3:
        print("num1 and num2 are equal and greatest")

    elif num3 > num1:
        print("num3 is Greatest")

    else:
        print("All Three Numbers are Equal")
else: 
    if num1 < num3:
        print("num3 is Greatest")
    elif num2 < num3:
        print("num3 is Greatest")
    else:
        print("All Three Numbers are Equal")
'''
'''       
#count a digit of a number.
a=int(input("Enter the number"))
count=0
while(a>0):
    a=a//10
    count=count+1
print(count)
'''

'''
 #1.wap to check user is eligible for vote or not??
 age=int(input("Enter the your age"))
 if(age>=18):
    print("your are eligible to for vote ")
else:
    print("you are not eligible for vote ")
    '''

'''
 #2.wap to check no. is +ve or -ve??
num=int(input("Entert the number"))
if(num<0):
    print("Number is nagative")
elif(num>0):
    print("Number is positive")
else:
    print("Number is zero")
'''
'''
 #3.wap to check no. is even or not??
num=int(input("Enter the number"))
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")
'''

'''
# 4.compare a no with 17 if no. is gretre than 17 then return absolute diff
#if not return square of diff??
num=int(input("Entert the number"))
diff=0
if(num>17):
    diff=num-17
    print(diff)
else:
    diff=(num-17)**2
    print(diff)
'''
 #5.comapre a 3 no. if all are equal then return
 #sum of all if not than return sum and thrice of all??
num1=int(input("Etner the number 1"))
num2=int(input("Etner the number 2"))
num3=int(input("Etner the number 3"))
if(num1==num2==num3):
    print(num1+num2+num3)
else:
    print(3*(num1+num2+num3))



'''
 6.comapre a two no. and find gretest b/w them?/
 7.take values  of length and breath of a rectangle from user and check
if it is square or not?/
 8.a company decided to give a bonus of 5% to
employee if the year of service is more than 5  years ask user for
their salary and year of service and print the net bonus??
 9.a student will not be allowed to sit in exam her
attendance is less than 75% take following input from user number of
classes held
,number of clasees attend is student to sit in exam or not??
//if_elif_else example
10.Traffic light
Write a python program that will check for the following conditions:
* If the light is green – Car is allowed to go
* If the light is yellow – Car has to wait
* If the light is red – Car has to stop
* Other signal – unrecognized signal. Example black, blue, etc…
11.Write a program to trace your subject mark. Your program should fulfill the following conditions:
1. If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
2. Students will fail in the subject if their mark is below 50.
3. Students will pass in the subject if they score 50 and above.
    1. If subject mark is between 50 and 60, grade student as good.
    2. If subject mark is between 60 and 80, grade student as very good.
    3. If subject mark is between 80 and 100, grade student as outstanding.
Make sure to print their mark in every statement to prove that the condition is fulfilled. Moreover, name, class, and section should be also displayed along with the marks and their grade.
12.Write a  program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

13.Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
findLargest()` finds the largest between two number by using “>” and “=” operator in JavaScript.
1. Print num1 is the largest if num1>num2.
2. Print num2 is the largest if num1<num2.
3. Else print num1 and num2 are equal when num1==num2.
14.Check if a triangle is equilateral, scalene, or isosceles
15.Find check if a year is leap year or not
16.`findGrade()` to find the grade of the student based on the input marks.
1. Print “S grade” if marks is between 90 and 100.
2. Print “A grade” if marks is between 80 and 90.
3. Print “B grade” if marks is between 70 and 80.
4. Print “C grade” if marks is between 60 and 70.
5. Print “D grade” if marks is between 50 and 60.
6. Print “E grade” if marks is between 40 and 50.
7. Print “Student has failed” if marks is between 0 and 40.
8. Else print “Invalid marks”.
17.Write a JavaScript program that displays the largest integer among two integers.

18. Write a JavaScript conditional statement to find the sign of the product of three numbers. Display an alert box with the specified sign.
Sample numbers : 3, -7, 2
19. Write a JavaScript conditional statement to sort three numbers. Display an alert box to show the results.
Sample numbers : 0, -1, 4
Output : 4, 0, -1

20. Write a JavaScript conditional statement to find the largest of five numbers. Display an alert box to show the results.
Sample numbers : -5, -2, -6, 0, -1

21. Write a JavaScript for loop that iterates from 0 to 15. For each iteration, it checks if the current number is odd or even, and displays a message on the screen.
Sample Output :
"0 is even"
"1 is odd"
"2 is even"


23. Write a JavaScript program to compute the greatest common divisor (GCD) of two positive integers.

24. Write a JavaScript program to sum 3 and 5 multiples under 1000.
25.Write a program that will allow someone to guess a four digit pin exactly 4
times. If the user guesses the number correctly. It prints “That was
correct!” Otherwise it will print “Sorry that was wrong.” Program stops after the 4th attempt of if they got it right.
26..Get the sum of two arrays…actually the sum of all their elements.
P.S. Each array includes only integer numbers. Output is a number too.
27. Print the ODD numbers from 7 to 31
28.Calculate the sum of all the numbers in the following array
var numbersArray = [1,13,22,123,49]
29. prints all the elements of a 2D array using nested for loops.
30.. Write a JS code to print Even numbers in given array
31.prints all the even numbers of a 2D array using for loops and ‘%’ operator.
32.Write a JS code to delete all occurrence of element in given array
33.Write a JS code to find the power of a number using for loop
34.Write a JS code to find the no of digits in a number
35.Write a JS code to calculate the sum of digits in a number
36.Write a JS code to find the largest number in an array
37.Write a JS code to find product of two arrays
38.Write a JS code to print the Fibonacci series for a given value of N
39.Write a JS code to find duplicate values in a given array
40.check no is pandriome or not?
41.check no is Armstrong or not?
42.check no is perfect or not??'''

