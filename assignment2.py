# EVEN OR ODD CHECK
#num = int(input("Enter a number: "))
#if (num % 2) == 0:
 #  print("{0} is Even".format(num))
#else:
 #  print("{0} is Odd".format(num))
#------------------------------------------------------------------------------------------------------
#LARGEST NUMBER CHECKING
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

#if (num1 >= num2) and (num1 >= num3):
 #  largest = num1
#elif (num2 >= num1) and (num2 >= num3):
  # largest = num2
#else:
   #largest = num3

#print("The largest number between",num1,",",num2,"and",num3,"is",largest)

#-----------------------------------------------------------------------------------------------------------------------------

#PRIME NUMBER CHECKING
#num = int(input("Enter a number: "))


#if num > 1:
 #   # check for factors
  #  for i in range(2, num):
   #     if (num % i) == 0:
    #        print(num, "is not a prime number")
#
 #           break
  #  else:
   #     print(num, "is a prime number")
#
# if input number is less than
# or equal to 1, it is not prime
#else:
 #   print(num, "is not a prime number")
#-------------------------------------------------------------------------------------------------------
#FACTORIAL NUMBER
#num = int(input("Enter a number: "))

#factorial = 1

# check if the number is negative, positive or zero
#if num < 0:
 #  print("Sorry, factorial does not exist for negative numbers")
#elif num == 0:
 #  print("The factorial of 0 is 1")
#else:
 #  for i in range(1,num + 1):
  #     factorial = factorial*i
   #print("The factorial of",num,"is",factorial)




#-------------------------------------------------------------------------------------------
#CHECK POSITIVE OR NEGATIVE
#num = float(input("Enter a number: "))
#if num > 0:
 #  print("Positive number")
#elif num == 0:
 #  print("Zero")
#else:
 #  print("Negative number")

 #---------------------------------------------------------------------------------------------------------------------------------------




# LEAP YEAR-----------------

#year = int(input("Enter a year: "))

#if (year % 4) == 0:
#   if (year % 100) == 0:
#       if (year % 400) == 0:
 #          print("{0} is a leap year".format(year))
 #      else:
  #         print("{0} is not a leap year".format(year))
 #  else:
 #      print("{0} is a leap year".format(year))
#else:
 #  print("{0} is not a leap year".format(year))

 #---------------------------------------------------------------------------------------------------------------------------------

 # SWAPPING WITHOUT 3RD VARIABLE
#x = int(input('Enter value of x: '))
#y = int(input('Enter value of y: '))



#x = x + y
#y = x - y
#x = x - y

#print('The value of x after swapping: ',x)
#print('The value of y after swapping: ',y)


#-------------------------------------------------------------------------------------------------------------------------------------------
#READING AND WRITING TO FILES

#f = open('myfile', 'w')
#f.write('hi there\n')

#f.close()



#f = open('myfile', 'r')
#if f.mode == 'r':
    #contents = f.read()
   # print(contents)

    #-----------------------------------------------------------------------------------
















