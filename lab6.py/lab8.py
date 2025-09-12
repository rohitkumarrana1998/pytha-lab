num=int(input("How many tems of series:,"))
# first two temss
a,b=0
count = 0
while count < num:
    print (a)
    a,b = b, a+b
    count += 1
