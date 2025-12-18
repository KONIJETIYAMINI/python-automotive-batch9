mylist={"apple", "banana", "cherry","apple",False, 0 ,2}
print(mylist)
#true=1
#false=1
mylist=['a','b']
myset2={"a","n"}
print(mylist)
empty_set=set()
empty_dict={ }
print(type(empty_set))
myset2.add(10)
mylist.discard(10)
mylist.update(mylist)
count=len(mylist)
print(mylist|myset2)
print(mylist&myset2)
for fruits in mylist:
    print("a fruit in the set:",fruits)
