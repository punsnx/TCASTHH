import random
x = random.randint(1,20)
y = random.randint(1,20)
z = random.randint(1,20)
t = x+y+z
if t > 50 :
    print("ได้",t,"pass",x,y,z)
elif t < 50 :
    print("ได้",t,"ขาดอีก",51-t,x,y,z)
else :
    print("ได้",t,"เท่ากัน",x,y,z)