import math

a= int(input("Enter launch angle (degrees): "))
d= int(input("Enter maximum distance (meters): "))
g= 9.8

rad= math.radians(a)

r= d*g
sin= 2*rad
sins= math.sin(sin)
v= r/sins 

vel= math.sqrt(v)

r_num= round(vel, 3)

print ("Required launch speed: ", r_num, "m/s")