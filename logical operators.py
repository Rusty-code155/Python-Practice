# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if not(temp>=0 and temp<=30):
     print("The weather is extreme!")
     print("stay inside")
elif not(temp< 0 or temp>30):
   print("The temperature is nice today")
   print("Go outside")
