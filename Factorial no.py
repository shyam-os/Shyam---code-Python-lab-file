# Q. Write a program to calculate the factorial of the given number

# By - Shyam Mandora 
# Date of Creation - 12-10-2021
# Last Modified - 12-10-2021

num = int(input("Enter positive Number: "))
fact=1
while(num>0):
    fact=fact*num;
    num-=1

print("Factorial of number = ", fact)

# Output: Enter positive Number: 5
#         Factorial of number =  120
