# slicing = creating a substring by extracting elements from another string
#               indexing[] or slice()
#                [start:stop:step]

name = "Turner Miles"
#Indexing
first_name= name[0:6]
middle_name=name[7:13]
print(first_name)
print (middle_name)
funky_name=name[0:13:2]
print(funky_name)
reversed_name=name[::-1]
print(reversed_name)
#Slicing
slice=slice(4,-6)
print(name[slice])