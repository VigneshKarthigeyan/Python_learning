ind=0
x=input("Enter the number you want to search: ")
list=[2,4,6,8,12,14,10]
def tosearch(list,num):
    for i in list:
        globals()['ind'] += 1
        if i==num:
            print("number found in list")
            return True
    else:
        print("number not found")
        return False
a=tosearch(list,int(x))
if a:
    print("At the index ",ind)
