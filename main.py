
#####x = int(input("insert value here:"))
######output = (x**2)+(2*x)+1
#####print(output)

# , is concate
# + is sum or concate


######LAb 1.1
##x = int(input("Insert here:"))
##output = x-543
##print(x,"=",output)


#####Lab1.2
###x = int(input("1.Insert point here:"))
###y = int(input("2.Insert point here:"))
###z = int(input("3.Insert point here:"))
#####output = (x+y+z)/3
###print("Total =",output)



######LAb1.3
####x = int(input("ปริมาณน้ำมัน:"))
####output = x*30
####print("ทั้งหมด",output,"บาท")

#####Lab1.4
###x = int(input("Insert value here :"))
###output = x**2
####print("Area","=",output)


#####Lab1.5
####x = int(input("Insert value here:"))
####output = (7/100)*x
####output_2 = x+output
###print("Vat","=",output)
###print("Total","=",output_2)

####output3 = 1.07*x
#output3 = (1 * x) + (0.07*x) >>> (1+0.07) * x
#####print("Total","=",output3)


#####Lab1.6
####x = int(input("Hours:"))
####z = int(input("Minutes:"))
####output =(x*3600)+(z*60)
###print("Input:","Hours:",x)
####print("Minutes:",z)
####print("Total :",output)
#x =int(input("insert here:"))
#n = x % 12
#y = x/12
#print(n)
#print(y)


# x = n % 5
# n = 1 - 30

#####Lab1.7
###x = int(input("Insert here:"))
#hour = int(x/3600)  ##### sec to  hour
#minute = int((x - (hour * 3600))/60)
#sec = x-(hour*3600)-(minute*60)

#hour = int(x/3600)  ##### sec to  hour
#minute = int((x % 3600)/60)
#sec = x % 60
#print(5000%3600)
#print("Value","=",x)
#print("HR","=",hour)
#print("Min","=",minute)
#print("Sec","=",sec)



#######if-else
##x = int(input("Enter Month ID here:"))
"""
if x == 1:
    print("This month have 31 days")
elif x ==2:
    print("This month have 28 days")
elif x ==3:
    print("This month have 31 days")
elif x ==4:
    print("This month have 30 days")
elif x==5:
    print("This month have 31 days")
elif x==6:
    print("This month have 30 days")
elif x==7:
    print("This month have 31 days")
elif x==8:
    print("This month have 31 days")
elif x==9:
    print("This month have 30 days")
elif x==10:
    print("This month have 31 days")
elif x==11:
    print("This month have 30 days")
elif x==12:
    print("This month have 31 days")

"""
"""
if x == 2:
  print("This month have 28 days")
elif x==1 or x==3 or x==5 or x== 7 or x== 8 or x==10 or x==12:
  print("This month have 31 days")
elif x==4 or x==6 or x==9 or x==11:
  print("This month have 30 days")
  """
  
  
  #####if-else 2
"""
x = int(input("Inset number here:"))
if x%3 == 0 :
  print("Correct")
else:
  print("incorrect")
"""

#####if-else 3
"""
x = int(input("Insert here:"))
if x >= 50000:
  y = x*0.1
  print("TAX:",y)
else:
  z = x*0.05
  print("TAX",z)
"""
  
######if-else 4
"""
a = int(input("Insert value A here:"))
b = int(input("Insert value B here:"))
 
if a > b :
   x_1 = (2*a**2)+(3*b)-5
   print("Ans is:",x_1)
else:
  x_2 = (b**2)-(3*a)
  print("Ans is:",x_2)
"""

####if-else 5 
##x = int(input("Insert here:"))
#if x>=10 and x <100:
 # print("Correct")
#else:
 # print("incorrect")
#####if-else 6 
"""
if x > 1 or x < -1 :
  print("correct")
else:
  print("incorrect")
"""

#####if-else 7
"""
x = int(input("Insert x here:"))
y = int(input("Insert y here:"))

if (x >= 1 and x <= 10) and (y>=1 and y<=100):
   print("correct")
else:
  print("incorrect")
"""
#####if-else 8
"""
user = str(input("Insert User here:"))
Pass = str(input("Insert Pass here:"))

if (user=="1002") and (Pass=="1234"):
  print("correct")
else:
  print("incorrect")
"""



######If-else day 2


####x= int(input("Insert score here:"))
"""
if x>=80 and x<=100:
  print("Your score is A")
elif x>=70 and x<= 79:
  print("Your score is B")
elif x>=60 and x<=69:
  print("Your score is C")
elif x>= 50 and x<= 59:
  print("Your score is D")
else:
  print("Your score is F")
"""
"""
if x>=80 :
  print("Your score is A")
elif x>=70 :
  print("Your score is B")
elif x>=60 :
  print("Your score is C")
elif x>= 50 :
  print("Your score is D")
else:
  print("Your score is F")
"""

######If-else day 2.2 
"""

Input_1 = input("Insert data here ")
Input_2 = int(input("Insert here"))

if Input_1 == "A" or Input_1=="C" or Input_1=="a" or Input_1=="c":
  cal = (Input_2*0.015)+Input_2
  
elif Input_1 == "B" or Input_1=="b":
  cal = (Input_2*0.02)+Input_2
  
elif Input_1 =="X" or Input_1=="x":
  cal = (Input_2*0.05)+Input_2
  
print("Total:",cal)
"""


#######If-else day 2.3
"""

name = input("Insert name here:")
age = int(input("Insert age here:"))
numDay1 = int(input("Insert working days here:"))
numDay2 = int(input("Insert absent days here:"))
kg = int(input("Insert body weight here:"))
print("Hi",name)
if age > 50:
  salary = numDay1*3000
elif age > 40:
  salary = (numDay1*1000)-(numDay2*25)
elif age > 30 :
  salary = (numDay1*500)-(numDay2*50)
elif age > 20:
  salary = (numDay1*300)-(numDay2*50)

print("Your salary is",salary,"Baht")
  
  
if kg <= 60 :
  salary = salary+5000
elif kg <=90:
  salary = salary+((5000)-(kg-60)*10)

  
  
print("Your salary and bonus is",salary,"Baht")
"""

#####If-else day 2.4
"""
x = int(input("Insert num1 here:"))
y = int(input("Insert num2 here:"))

if x > 6 or y > 6 :
  print("Out of bound")
elif x < 7 and y < 7:
  if x+y > 6 :
    print("High")
  else: 
    print("Low")
"""
""""
x = int(input("Insert your monitor size 38 or 43 only:"))
price = 375.99


if x == 38 :
  price = price+75.99
  print(x,"monitor")
  y = int(input("Do you want DVD-ROM? 1 is yes / 0 is No:"))
  
elif x == 43 :
  price = price+99.99
  print(x,"monitor")
  y = int(input("Do you want DVD-ROM? 1 is yes / 0 is No:"))

if y ==1 :
  price = price+65.99
  print("DVD>>>65.99")
  z = int(input("Do you want printer? 1 is yes / 0 is no:"))


if z ==1:
  price = price+125
  print("Printer>>>125")
  

print("===My order===")

print("===Total price>>>",price)

"""
####Loop 1 
"""
x = int(input("Insert number here:"))


for i in range (1,13):
  print(x,"*",i,"=",(x*i)) 

"""
####Loop 2
""" 
for i in range(x):
  print("#-#-#-#-#")
"""

####Loop 3
""" 
for i in range(x):
  if i % 2 > 0 :
    print(i)

for i in range(1,x,2):
  print(i)
"""
#####Loop 4
"""
for i in range(1,x+1):
  if i % 5 > 0 :
    print("|",end="")
  else:
    print("|",end="")

"""
"""
for i in range(1,x+1):
  if i % 5 > 0 :
    print("|",end="")
  else:
    print("|",end="\n")
"""
####Loop 5
"""
firstNum = x
while x % 3 > 0 and x % 2 > 0:
  x = int(input("Insert number here:"))
    
print(firstNum)
"""
"""
x = int(input("Insert number here:"))
y = int(input("Insert number here:"))
print("Addition:",x+y)
print("เชืื่อม:",str(x)+str(y))
"""
######Loop 6
"""
x = int(input("Insert number here:"))
y = input("Insert Cha here:")
z = input("Insert Cha here:")

for i in range(1,x+1):
  if i % 2 > 0:
    print(y,end="")
  else:
    print(z,end="")
"""
########
"""
x = float(input("Insert Weight here:"))
y = float(input("Insert height here:"))
z = x/y**2

if z < 18.5 :
  print("Underweight")
elif z < 25:
  print("Normal weight")
elif z < 30 :
  print("Overweight")
else:
  print("Obesity")
"""
"""
x = int(input("Insert here:"))
y = int(input("Insert here:"))
print("*\n**\n***")
for i in range(1,x+1):
  print("###")
print("@@@")

for a in range(1,y+1):
  print("###")

print("***\n**\n*")
"""
#####LOOp 6
"""
x = int(input("Insert here:"))
i = 0
z = 0
while x != -1:
 
  if x % 2 == 0 :
    i =i+1
  else:
    z = z+1
  x = int(input("Insert here:"))
    
    

print("Odd:",i,end=" ")
print("Even:",z)

"""
#####Loop 8 
"""
x = int(input("Insert here:"))###1

y = x ####1

while x - y < 5 and y - x < 5:
  y = x
  x = int(input("Insert here:"))
print("finish")
"""
#####Loop 9
"""
x = int(input("Insert here:"))
maxValue = x

while x != -1:
  if x > maxValue:
    maxValue = x
  x = int(input("Insert here:"))

print(maxValue)
"""
######Loop 10
"""
x = int(input("Insert here:"))
y = x
####area = x*y
for i in range(1,x+1):
  print("")
  for z in range(1,y+1):
    print("#",end="")
"""
####Loop 11
"""
x = int(input("Insert here:"))
for i in range(1,x+1):
  print("")
  for z in range(1,i+1):
    print("#",end="") 
"""

#####Loop 12

"""

x = int(input("Insert here:"))
y = x
for i in range(1,x+1):
   print("")
   for z in range(i,x+1):
     print("#",end="")
"""

######Loop 13
"""
x = int(input("Insert here:"))
for i in range(1,x+1):
  print("")
  for z in range(i,x):
    print(" ",end="")
  for y in range(1,i+1):
    print("#",end="")
"""



######Loop 14
"""
x =  int(input("Insert here:"))### Y Axis
y = int(input("Insert here:"))### X Axis

for i in range(1,x+1):
  print("")
  for z in range(1,y+1):
    print("X",end="")
"""
#####Loop 15
"""
x = int(input("Insert here:"))

for i in range(1,x+1):
  print("")
  for z in range(0,i):
    print(" ",end="")
  for y in range((2*i),(2*x)+1):
    print("*",end="")
"""

###Loop 16 
"""
x = int(input("Insert here:"))

for i in range(1,x+1):
  print("")
  for z in range(i,x):
    print("1",end="")
  for y in range(1,i*2):
    print("2",end="")
  for q in range(i,x):
    print("3",end="")
"""

x = int(input("Insert Here:"))

for i in range(1,x+1):
  print("")
  for z in range(1,x+1):
    print("A",end="")
  print("0",end="")
  for y in range(1,x+1):
    print("B",end="")
print("")

for g in range(0,2*x+1):
  print("X",end="")
for i in range(1,x+1):
  print("")
  for z in range(1,x+1):
    print("C",end="")
  print("0",end="")
  for y in range(1,x+1):
    print("D",end="")
 


####Function1.1
"""
import math

def decom(a,b,c):
  x = (b**2)+ (math.sqrt(4*a*c))
  neg_1 = (b**2)- (math.sqrt(4*a*c))
  val = x/(2*a)
  val_neg = neg_1/(2*a)
  return val, val_neg

def even_check(number):
  if number%2 == 0:
    return True
  return False

def tri(input):
  total = 0
  for i in range(1,input+1):
    print("")
    for z in range(1,i+1):
      print("*",end="")
      total = total+1
  return (total)
         

def fac(number):
  total = 1
  if number < 0 :
    return 0
  for i in range(1,number+1):
    total = total*i
  
  return total
  
def sort_num(a,b,c):
  if a>b and a>c:
    if b > c :
      return a,b,c
    else:
      return a,c,b
  elif b>a and b>c:
    if a>c:
      return b,a,c
    else:
      return b,c,a
  elif c>b and c>a:
    if b>a:
      return c,b,a
    else:
      return c,a,b
  
 

def num_2(number):####หาจำนวนเฉพาะ
  for i in range(2,number):
    if number%i == 0:
      return False
  return True
    
     
    

def check_num(number):
  total = 0
  for i in range(1,number+1):
    if num_2(i):
      total =total+1

  return fac(total)
      
n1 = check_num(7)

print(n1)
"""


####str1.1
"""

x = input("Insert here:")
yes = "y"
no = "n"

if x == yes or x == yes.upper():
  print("Yes")
elif x == no or x == no.upper():
  print("No")
else:
  x = input("Insert Here:")
"""
###str1.2
"""
x = input("Insert mail here:")

if  "@"in x:
  value =  x.find("@",0)
  val = x[0:value]
  print("Hello",val)
"""
####str1.3
"""
x = input("Insert mail here:")

if  "@"in x:
  value =  x.find("@",0)
  val = x[value+1:]
  print("www."+val)
"""
####str1.4
"""
s = input("Insert sentence :")
count = 0;

for i in range(len(s)):
  if s[i] == " ":
    count = count + 1;
print("there are",(count+1), " words.")
"""

####str1.5
"""
s = input("Insert sentence :")

if "a" in s.lower():
  print("A ")
if "e" in s.lower():
  print("E ")
if "i" in s.lower():
  print("I ")
if "o" in s.lower():
  print("O ")
if "u" in s.lower():
  print("U ")
"""

####Lists
"""
numArr2 = [9,7,5,3,1,-1,3,5,7]
chArr1 = ["A","L","E","X"]
stringArr1 = ["Adam","Alex","Bank","peter","sara","pop"]
doubleArr = [3.2,4.057,9.81,7.2451]
booleanArr1 = [True,False,False,True]
"""
"""
print(numArr2)
print(chArr1)
print(stringArr1)
print(doubleArr)
print(booleanArr1)
"""

#####List 2
n = [2,7,4,3,8,0,9,5,6]
"""
for i in range(len(n)):
  x = n[i]
  print(x)
"""
"""
for i in n:
  if i%2 != 0:
    print(i)
"""

####x = int(input("insert here:"))
"""
y = 0
for i in n:
  y = y+i
  if y > x :
    break
  else:
    print(i)
"""
"""
y = 0

while x != -1:
  n.append(x)
  print(n)
  x = int(input("insert here:"))
print(n)

for i in n :
    if i > y :
      y = i
      
print(y)


"""

"""
arr1 = []
for i in range(1,11):
  arr1.append(x)
  print(arr1)
  x = int(input("insert here:"))
y = 0
for i in arr1:
  val = y+i
  y = val

print(val)
total = val/10
print(total)
for i in arr1:
  if i > total:
    val = i
print("Max",val)
"""
"""
nsum = 0;
nmax = 0;
arr1 = []
for i in range(1,11):
  arr1.append(x)
  print(arr1)
  nsum = nsum + x;
  if nmax < x:
    nmax = x
  x = int(input("insert here:")) 
 
print("mean : ", (nsum/10))
print("max : ", nmax)



x = input("Insert here:")
vowels = ["a","e","i","o","u"]
vocab = x.lower()
vocab_1= vocab.split(" ")
h = ""
for m in vocab_1:
  h = h+m
print(h)
  

  
y = 0
r = 0
for i in h:
  if i in vowels:
    y = y+1
  else:
    r = r+1



import random

x = input("Insert here:")
vowels = ["a","e","i","o","u"]
vocab = x.lower()

y = 0
r = 0
for i in vocab:
  if i in vowels:
    y = y+1
  elif i != " ":
    r = r+1
    
  


print("vowels:",y)
print("Not vowels:",r)

def checkVowels(y):
  vowels = ["a","e","i","o","u"]
  for tmp in y:
    if tmp in vowels:
      return True;
  return False;

x = int(input("Insert here:"))
print("x is ", x)

arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]
y= ""

while not checkVowels(y) :
  y = ""
  x0 = x
  print("round")
  
  while x0 > 0:
    n = random.randint(1,25)
    arr_val = arr[n]
    if arr_val not in y:
      y = y + arr_val
      x0 = x0 - 1


print(y)


y = int(input("Enter guess(0-100):"))
x = random.randint(0,100)


while y != x:
  if  y < 0 or y >100:
    print("Out of range")
    y = int(input("Enter guess(0-100):"))
  elif y > x :
    print("Too high")
    y = int(input("Enter guess(0-100):"))
  elif y < x:
    print("Too Low")
    y = int(input("Enter guess(0-100):"))
print("ANS =",x)
  
  


    
"""


  





  
  
    

   
  

 


    
    
