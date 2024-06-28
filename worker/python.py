#odd/even
# number=int(input("Enter a number:"))
# if(number%2==0):
#     print("{0} is Even".format(number))
# else:
#     print("{0} is Odd".format(number))

#positive/negative:
# num=float(input("enter a float number:"))
# if num>0:
#     print("positive number")
# elif num==0:
#     print("zero")
# else:
#     print("negative number")

#prime/not'
# num=int(input("enter a num:"))
# prime=False
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             prime=True
#             break
        
# if prime:
#     print(num,"is not a prime number")
# else:
#     print(num,"is a prime number")                
            
            
#palindrome
# def palindrome(s):
#     return s==s[::-1] 
# s="pop"
# ans=palindrome(s)
# if ans:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome") 

#maximum of two numbers & minimum of two numbers:
# def maximum(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# a=int(input())
# b=int(input())
# print(maximum(a,b))

# def minimum(a,b):
#     if a<=b:
#         return a
#     else:
#         return b
# a=int(input())
# b=int(input())
# print(minimum(a,b))     
                          
#factorial:
# def factorial(n):
#     return 1 if (n==0 or n==1) else n*factorial(n-1)
# num=5
# print("factorial of ",num,"is",factorial(num)) 

#fibonacci series:
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,100):
#     sum=a+b
#     print(sum)
#     a=b
#     b=sum
a=[10,15,35,40,95,99]
print("the largest element in the list is",max(a))
print("the smallest number in the given list is",min(a))
                             