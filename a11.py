s=5
if(type(s)is int):
    print("true")
else:
    print("false")
s=5.5
if(type(s)is not float):
    print("true")
else:
    print("false")
s=19
r=19
if(s is r):
    print("same identity")
r=8
if(s is not r):
    print("both dont have same identity")
j=16
p=16
print("j>>1:",j>>1)
print("p<<1:",p<<1)
print("marks obtained")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
avg=int(total/5)
valid_range=range(50,90)
if avg not in valid_range:
    print("invalid")
elif avg is (70,90):
    print("you got a grade")
elif avg is (1,50):
    print("you got b grade")
else:
    print("study well!")