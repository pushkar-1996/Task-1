import sys
b=[]
final=[]
empty=[]
a=input("enter the sentence")
c=input("enter the required integer")
v=abs(int(c))
if int(v)<=25:
      p=v
else:
      p=int(v)%26
b=a.split()
#print(b)
for i in range(len(b)):
    for j in b[i]:
        x=ord(j)+ int(p)
        if 65<=x<=90 or 97<=x<=122:
            k=chr(x)
        else:
            k=chr(x-26)
        empty.append(k)
        g=''.join(empty)
    final.append(g)
    empty.clear()
g = None
#print(final)
print(' '.join(final))

        
