a=int(input())
b=int(input())
c=int(input())
if(a<b) and (a<c):
    print("Smallest number:",a)
elif(b<a and b<c):
    print("Smallest number:",b)
elif(c<a and c<b):
    print("Smallest number:",c)
else:
    print("Input are equal")
