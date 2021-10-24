#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a Python program to print the following string in a specific format (see the
# output). 
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[3]:


# Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)


# In[4]:


# 3. Write a Python program to display the current date and time. 
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	


# In[5]:


# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[6]:


# 5. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
firstName= input("Enter fistname");
lastName = input("Enter lastname");

print ("Hello  " + lastName + " " + firstName)


# In[7]:


# 6. Write a python program which takes two inputs from user and print them addition
num1 =  input("Enter firstValue");
num2 = input("Enter SecondtValue");

# Add two numbers
sum = num1 + num2

# Display the sum
print(sum)


# In[8]:


# Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ? 
eng = int(input("Enter English Marks"));
isl = int(input("Enter Islamiat Marks"));
maths = int(input("Enter Maths Marks"));
phy = int(input("Enter Physics Marks"));
chem = int(input("Enter Chemistry Marks"));
total = 500;
percent = (eng + isl + maths +phy + chem)/total*100;
if percent < 100 and percent >= 80:
    print("A+");
elif percent < 80 and percent >= 70:
    print("A");
elif percent < 70 and percent >= 60:
    print("B");
elif percent < 60 and percent >= 50:
    print("C");
elif percent < 50 and percent >= 40:
    print("D");
elif percent < 40 and percent >= 33:
    print("E");
elif percent < 0 and percent > 100:
    print("You didnot write correct percent");
else:
    print("Fail")


# In[9]:


# Write a program which take input from user and identify that the given number is even
# or odd? 
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[10]:


# 9. Write a program which print the length of the list? 
ListName = ["Hello", "ariba", 1, 2, 3]
print ("Number of items in the list = ", len(ListName))


# In[ ]:


# .Write a Python program to sum all the numeric items in a list?
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[ ]:


# Write a Python program to get the largest number from a numeric list. 
list1 = [10, 20, 4, 45, 99]
  
  
# printing the maximum element
print("Largest element is:", max(list1))


# In[ ]:


# 12. Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  Write a program that prints out all the elements of the list that are less than 5
test_list= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in test_list:
    if(int(element) <5):
        print(str(element)+"\n")


# In[ ]:




