x=input("Enter list of strings with space b/w them: ")
lst=x.split()
for i in lst:
    count=0
    for j in i:
        count+=1
    print("string - ",i,count)