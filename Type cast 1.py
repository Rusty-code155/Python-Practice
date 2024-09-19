#Type Casting: Converts data types of a value to another data type
x=1 #Type: int
y=1.23 #Type: Float
z=("Jeff") #Type: String
response=True # Type Boolean
print(type(x))
print(type(y))
print(type(z))
print(type(response))
#Type cast
print(type(str(x)))
print(type(int(y)))
print(type(str(response)))
#Note: String only functions for the type cast if the variable value is equivalent to the type of the conversion
#Perminate type cast
x=float(x)
y=int(y)
print(type(x))
print(type(y))