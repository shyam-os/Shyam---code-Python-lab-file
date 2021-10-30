# Q. Write a program to input 8 numbers from the user and display all the unique numbers (once).
# By - Shyam Mandora
# Date of Creation - 30-10-2021
# Last Modified - 30-10-2021
# code
A = []
print("Enter the Element of List :")
for i in range(8):
    A.append(input(""))

print("The unique values from the List is :", set(A))

# Output : Enter the Element of List :
#             1
#             2
#             3
#             5
#             2
#             3 
#             4
#             6
#             The unique values from the List is : {'2', '3', '5', '1', '6', '4'}
