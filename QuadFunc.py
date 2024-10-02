import math  #Necessary import

p=int(input("calc? 1/0"))  #Loop Start

while p==1:
  print("Quadratic Function")
  
  a=int(input("a = "))  #Info
  b=int(input("b = "))
  c=int(input("c = "))
  
  de=b**2-4*a*c  #Calculation N1
  
  print(" ")  #Printing var start
  print("Delta=")
  print(de)
  print("      ")  #End
  
  if de<0:
    print("Unsolvable")
    p=int(input("1 to cont:"))  #While Loop line 5
    
  elif de==0:
    sol1=(-b)/(2*a)  #Calculation N2.1
    sol11=(-b)
    sol12=(2*a)
    
    print("Solvable 1sol")  #Printing the result start
    print(" ")
    print(sol11)
    print("------")
    print(sol12)
    print(" ")
    print(sol1)  #End
    
    p=int(input("1 to cont:"))  #While Loop line 5
    
  elif de>0:
    s=math.sqrt(de)  #Calculation N2.2
    sol1=(-b+s)/(2*a)
    sol11=(-b+s)
    sol2=(-b-s)/(2*a)
    sol22=(-b-s)
    p=2*a
    
    print("Solvable 2sol")  #Printing the result(s) start
    print(sol11)
    print("------")
    print(p)
    print("      ")
    print(sol1)
    print("      ")
    print(sol22)
    print("------")
    print(p)
    print("      ")
    print(sol2)  #End
    
    p=int(input("1 to cont:"))  #While loop line 5
    
  else:
    print("Error")  #In case of error stop While Loop
    break
