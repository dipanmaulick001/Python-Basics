#Count the no of positive nos in a list
#numbers = [1,-2,3,-4,5,6,7,8-9-10]
#positive_count = 0
#for num in numbers :
    #if num > 0 :
        #positive_count = positive_count + 1
#print("The number of positive numbers:",positive_count)


#Sum of even nos upto n
#n = int(input("Enter n : "))
#sum_even = 0
#for i in range(n):
    #if i%2 == 0:
        #sum_even=sum_even + 1
#print("Sum of even numbers : ",sum_even)

#print multiples of a no upto 10 but skip the 5th iteration 
#m = 4
#for i in range(1,11):
    #if i==5:
        #continue
    #print(m,"X",i,"=",m*i)

#reverse a string using a loop
#input_str = 'Python'
#reversed_str = ''
#for char in input_str:
#    reversed_str = char + reversed_str
#print("Reversed string is : ",reversed_str)

#find first non repeated character 
#input_strr = "mississipie"
#for char in input_strr:
    #if input_strr.count(char)==1:
        #print("",char)

#factorial
#number = 5
#abc = number
#factorial = 1 
#while number > 0:
    #factorial = factorial*number
    #number = number - 1
#print("Factorial of",abc,": ",factorial)


#validate ip. keep asking user for input until they enter between 1 and 10
#while True :
    #x = int(input("Enter : "))
    #if 1 < x < 10 :
        #print("Accepted")
        #break
    #else :
        #print("Invalid, enter again")

#Prime no checker 

#xx = int(input("Enter : "))
#is_prime = True 
#if xx > 1:
#    for i in range(2,xx):
 #       if (xx%i)==0:
#            is_prime = False
#            break
#print(is_prime)

#check if all elemts in a list are unique if duplicate foumd, exit loop and print the duplicate

#items = ['apple','banana','orange','apple','mango','banana']
#unique_items = set()

#for item in items :
    #if item in unique_items:
        #print(item)
        #exit
    #unique_items.add(item) 

#implement strategy that doubles wait time bw retries , starting from 1 second, but stops after 5 retries 
import time 
wait_time = 1
attempts = 0
max_attempts = 5

while attempts <= max_attempts :
    print("Attempt no : ",attempts,"Wait time: ",wait_time)
    time.sleep(wait_time)
    wait_time = wait_time*2 
    attempts = attempts + 1