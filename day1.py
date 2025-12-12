
n=int(input("Enter a number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

n=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if n>b:
    print("Greater")
else:
    print("Lesser")
    

for i in range(1,11):
    print(i)
  
    
a=10
b=20
print("sum=",a+b)
with open("example.txt","r")as f:
    content=f.read()
    print(content)
    


num = int(input("Enter a number: "))


if num > 1:
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

numbers = [10, 25, 3, 99, 56]

