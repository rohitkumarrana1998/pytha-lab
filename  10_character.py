t = input("Enter a string:")
count = { }
for char in t:
    count [char]=count.get (char ,0) +1 
    print(count)