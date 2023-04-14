s=int(input("Enter the correct readings "))
p=int(input("Enter previous readings "))
units=s-p 
if units<=200:
    total =units*3.0
elif units <= 250:
    total=(200*3.0)+(units-200)*4.5
elif units<=400:
    total=(200*3.0)+(50*4.5)+(units-250)*6.5
else:
    total=(200*3.0)+(50*4.5)+(150*6.5)+(units-400)*7.0
print(f"Bill= {total}")