univ="amrita vishwa vidyapeetham"
print(univ)
count=0
for ch in univ:
   if(ch=='a' or ch=='A'):
        count=count+1
print(count)

num=0
for ch in univ:
    if ch in ['a','e','i','o','u']:
        num=num+1
print(num)

num=0
for ch in univ:
    if ch not in ['a','e','i','o','u',' ']:
        num=num+1
print(num)

x="I belong in section CSE F"

x=x.split(sep=' ')
for i in range(0,6):
    if i%2!=0:
        x[i]=x[i].upper()
print(x)

y="In social media, a story is a function in which the user tells a narrative or provides status messages and information"

y=y.split(sep=' ')
for i in range(0,21):
    if i%3==0:
        if i in ['a','e','i','o','u']:
            y[i]=y[i].upper()
        else:
            break
print(y)
