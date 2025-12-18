mystring="abcdefghijklmnop"
sub1=mystring[0:6] #slice the first 7 elements
sub2=mystring[7: ] #from the 7th 
sub3=mystring[:5]
sub4=mystring[10]
sub5=mystring[-5]
if "a" in mystring:
    print("a is there")

word=mystring.split(" ")
print(word)
mystring.upper()
mystring.lower()
print(mystring+"m")