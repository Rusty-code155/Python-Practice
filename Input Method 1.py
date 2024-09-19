#Inputs allow for user data to be processed through the code
#Start with a String value in order to ask the question/prompt
name=input("What is your name?")
age=int(input("How old are you?"))
height= float (input("How tall are you?"))
print("My name is"+name+" and I am "+str(age)+ " years old." +"\n I am " + str(height) +" feet tall.")
age=age+1
print("After my birthday I will be "+ str(age) + " years old")