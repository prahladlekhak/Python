"""print("helloworld")"""
import random

"""tokens=smallest individual unit of a program
keywords
literals
punctuators
identifiers
operators"""

# n=int(input("enter the number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
'''num=int(input("enter the number: "))
n=1
while(n<=10):
    print(num,"*",n,"=",num*n)
    n+=1'''

"""n=int(input("Enter the number: "))
count=0
sum=0
while(n!=0):
    a=n%10
    n=n//10
    sum=sum+a
    count+=1
print("count is: ",count,"sum is: ",sum)"""


'''num=int(input("enter the number"))
for i in range(1,num+1):
    count=0
    for j in range(i,0,-1):
        if i%j==0:
        break
            count+=1
    if count==2:
        print(j,"the number is prime")
    else:
        print(j,"is composite")'''



'''a=int(input("enter the number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)'''


"""a=int(input("enter the number"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""


"""a=int(input("enter the number"))
for i in range(1,a+1):
    for j in range(a-i+1):
        print("*",end=" ")
    print()"""





'''a=int(input("enter the number"))
for z in range(1,a):
    for b in range(a-z+1):
        print(" ",end=" ")
    for c in range(2*z-1):
        print("*",end=" ")
    print()
for z in range(5,0,-1):
    for b in range(a-z+1):
        print(" ",end=" ")
    for c in range(2*z-1):
        print("*",end=" ")
    print()'''







"""s=("veni vedi veci")
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.lower())"""




"""a=int(input("enter the number: "))
for i in range(a+1,1,-1):
    for j in range(a+1-i):
        print(" ", end=" ")
    for k in range(2*i-3):
        print("*", end=" ")
    print()"""



'''l=[1,2,3]
m=[3,4,6]
n=[]
for i in range(3):
    val=l[i]+m[i]
    n.append(val)
print(n)'''


#file handling
'''f=open("text.txt","r")
str=" "
vcount=1
ccount=0
while str:
    str=f.read(1)
    if str in ["a","e","i","o","u","A","E","I","O","U"]:
        vcount+=1
    else:
        ccount+=1
print(vcount)
print(ccount)'''




'''f=open("text.txt","r")
str=" "
while str:
    str=f.readline()#lines will print everything in the form of list and in the same line
    print(str,end="")'''


'''f=open("blue.txt","w")
for i in range(5):
    name=input("Enter the name: ")
    f.write(name+"\n")'''

#in append data doesnt get deleted ,,add hojata hai

#list.append(name+"\n)
#f.close() data save hojata hai


"""f=open("blue.txt","w")
list=[]
for i in range(5):
    rollno=int(input("Enter the number: "))
    name=input("Enter the name: ")
    marks=float(input("Enter marks: "))
    list.append("roll no:" +str(rollno) + ",and name:"+name +",has got marks: "+str(marks)+"\n")
f.writelines(list)"""


'''def chkno(n):
    if n%2==0:
        print("no is even")

    else:
        print("the number is odd")
n=int(input("Enter the number"))
chkno(n)'''


'''def prime(num):
    for i in range(1,num+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+= 1
        if count== 2:
            print(j, "the number is prime")
        else:
            print(j, "is composite")
num=int(input("enter the number"))
prime(num)'''





'''def d2rn(d):
    return d*82,"rupees"
def d2rv(d):
    print("the amount in rupees is: ",d*82)
d=int(input("enter the number"))
print(d2rn(d))
d2rv(d)'''



'''def volume(l,b,h):
    return l*b*h
l=int(input("Enter the number: "))
b=int(input("Enter the number: "))
h=int(input("Enter the number: "))
print(volume(l,b,h))'''



'''def m(a,b):
    if a==b:
        print("True")
    else:
        print("False")
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
m(a,b)'''

#import random
"""def num(a,b):
    print(random.randint(a,b))
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
num(a,b)"""

'''a=input("Enter the string: ")
b=input("Enter the string: ")
def string(a,b):
    return
if len(a)==len(b):
    print("True")
else:
    print("False")

string(a,b)'''




'''def nthRoot(x,n):
    return
x=int(input("enter the number: "))
n=int(input("enter the number: "))
if n==0:
    print(x**1/2)
else:
    print(x**1/n)
nthRoot(x,n)'''


'''import random
def rdm(n):
    return random.random()
n=int(input("Enter the number:"))
print(rdm(n))'''



'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number: "))
print(fact(n))'''


'''def sum(n):
    if n==1:
        return 1
     else:
        return n+sum(n-1)
n=int(input("Enter the number: "))
print(sum(n))'''



'''num=int(input("Enter the number: "))
sum=0
org=num
while num!=0:
    r=num%10
    sum=sum*10+r
    num=num//10
if org==sum:
    print("The number is palindrome")
else:
    print("The number is not palindrome")'''



#fibonacci series
'''def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
n=int(input("Enter the number: "))
print(f(n))'''


#fibonacci sequence
'''n_terms = int(input ("How many terms the user wants to print? "))
n_1 = 0
n_2 = 1
count = 0
if n_terms<0:
    print ("Please enter a positive integer, the given number is not valid")
elif n_terms == 1:
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")
    print(n_1)
else:
    print ("The fibonacci sequence of the numbers is:")
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1'''





"""a=int(input("Enter the value: ")) prime  number program
for i in range(1,a+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)"""




'''a=int(input("Enter the number :"))
r=0
while a!=0:
    r=a%10
    a=a//10
    print(r,end="")'''


# import pyautogui as p
# import time
# message=input("enter your message ")
# limit=input("enter the limit")
# i=0
# time.sleep(5)
# while i<int(limit):
#     p.typewrite(message)
#     p.press("enter")
#     i+=1



'''for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=" ")
    print()'''

"""a=input("enter your name: ")
b=int(input("enter your age:"))
cy=2023
m=100-b
i=cy+m
print("you will celebrate century on year",i)"""


"""list=[2,3,7,5,7,9]
li=[]
for i in range(len(list)):
    for j in range(i+1,len(list)-1):
        if list[i]==list[j]:
            list.remove(list[i])
        else:
            li.append(list[i])

print(li)"""




"""str= input("enter")
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")"""



"""a=input("enter the alphabet: ")
count=0
for i in a:
    count+=1
print(count)"""


"""list=["prahlad","palak","rahul","harshwardhan"]
list.insert(1,"hello")
print(list)"""



"""str="this python programming"
add=input("enter the substring: ")
n=int(input("enter the position you want to insert the substring: "))
str1=[]
for i in range(len(str)):
    str1.append(str[i])
str1.insert(n," "+add)
hey="".join(str1)
print(hey)"""

"""list=["bobby","palak","mannu","rahul","harshwardhan","kailash"]"""

"""a=input('enter the alphabet')
alphabet=0
digit=0
space=0
for i in range(len(a)):
    if a[i].isalpha():
        alphabet+=1
    elif a[i].isdigit():
        digit+=1
    elif a[i].isspace():
        space+=1
print(digit,"digits")
print(alphabet,"alphabets")
print(space,"no of space")"""


"""a=int(input("enter the number"))
while a!=0:
    b=a%10
    a=a//10
    print(b,end="")"""


"""def leap(a):
    if (a%4==0 and a%100!=0 or a%400==0):
        print(a,"is a leap year")
    else:
        print(a,"is not a leap year")

a = int(input("enter the year: "))
leap(a)"""

"""nterms = int(input ("no of terms you want to print:"))
def fib(nterms):
    n1 = 0
    n2 = 1
    count = 0
    if nterms<0:
        print ("Please enter a positive integer, the given number is not valid")
    elif nterms == 0 or nterms==1:
        print ("the sequence upto", nterms, "is : ",n1)
    else:
        print ("sequence of the numbers upto",nterms,"terms is: ")
        while count<nterms:
            print(n1,end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count+=1

fib(nterms)"""

"""import random

def range(a):
    print(random.randint(a**(a-1),10**a))

a=int(input("enter the number of digits"))
range(a)"""



"""a=int(input("enter the number"))
for z in range(1,a):
    for b in range(a-z+1):
        print(" ",end=" ")
    for c in range(2*z-1):
        print("*",end=" ")
    print()
for z in range(5,0,-1):
    for b in range(a-z+1):
        print(" ",end=" ")
    for c in range(2*z-1):
        print("*",end=" ")
    print()"""



'''mat1=[[],[],[]]
mat2=[[],[],[]]
mat3=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input("enter the number: "))
        mat1[i].append(a)
for i in range(3):
    for j in range(3):
        a=int(input("enter the number: "))
        mat2[i].append(a)
for i in range(3):
    for j in range(3):
        s=mat1[i][j]+mat2[i][j]
        mat3[i].append(s)
print(mat3)'''



'''mat1=[[],[]]
mat2=[[],[]]
mat3=[[],[]]
for i in range(2):
    for j in range(2):
        a=int(input("enter the number: "))
        mat1[i].append(a)
for i in range(2):
    for j in range(2):
        a=int(input("enter the number: "))
        mat2[i].append(a)
for i in range(2):
    for j in range(2):
        sum=0
        for k in range(2):
            s=mat1[i][k]*mat2[k][j]
            sum+=s
        mat3[i].append(sum)
print(mat3)'''



'''def pal(a):
    arm=0
    while a!=0:
        r=a%10
        arm=arm+r*3
        a=a//10
a=int(input("enter the number: "))
pal(a)'''


# a=int(input("enter the number"))
# for i in range(a):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# a=int(input("enter the number"))
# for i in range(a):
#     for j in range(a-i):
#         print("*",end=" ")
#     print()


# a=int(input("enter the number"))
# for i in range(a):
#     for j in range(i):
#         print("+",end=" ")
#     print()
# for i in range(a):
#     for j in range(a-i):
#         print("+",end=" ")
#     print()



# a=int(input("Enter the number: "))
# for i in range(1,a+1):
#    for j in range(1,a+1):
#        if i==1 or i==5 or j==1 or j==5 :
#            print("*",end="  ")
#        else:
#            print("  ",end=" ")
#            print()

# a=int(input("Enter the number: "))
# for i in range(a,0,-1):
#    for j in range(1,i+1):
#            print("*",end="  ")
#    print()


# a=int(input("Enter the number: "))
# for i in range(a):
#    for j in range(a-i):
#        print("*",end=" ")
#    for k in range(i):
#        print("  ",end="  ")
#    for l in range(a-i):
#         print("*",end=" ")
#    for j in range(a-i):
#        print("*",end=" ")
#    for k in range(i):
#        print("  ",end="  ")
#    for l in range(a-i):
#         print("*",end=" ")
#    for j in range(a-i):
#        print("*",end=" ")
#    for k in range(i):
#        print("  ",end="  ")
#    for l in range(a-i):
#         print("*",end=" ")
#    for j in range(a-i):
#        print("*",end=" ")
#    for k in range(i):
#        print("  ",end="  ")
#    for l in range(a-i):
#         print("*",end=" ")
#    for j in range(a - i):
#        print("*", end=" ")
#    for k in range(i):
#        print("  ", end="  ")
#    for l in range(a - i):
#        print("*", end=" ")
#    for j in range(a - i):
#        print("*", end=" ")
#    for k in range(i):
#        print("  ", end="  ")
#    for l in range(a - i):
#        print("*", end=" ")
#    for j in range(a - i):
#        print("*", end=" ")
#    for k in range(i):
#        print("  ", end="  ")
#    for l in range(a - i):
#        print("*", end=" ")
#    for j in range(a - i):
#        print("*", end=" ")
#    for k in range(i):
#        print("  ", end="  ")
#    for l in range(a - i):
#        print("*", end=" ")
#    print()
# for i in range(1,a+1):
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    for j in range(i):
#        print("*",end=" ")
#    for k in range(a-i):
#        print("  ",end="  ")
#    for l in range(i):
#         print("*",end=" ")
#    print()


#
# a=5
# if a==4:
#     a=a+3
# else:
#     print(a)