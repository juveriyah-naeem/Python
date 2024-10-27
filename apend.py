
# list=[]
# a=input("Enter 1st movie name:")
# b=input("Enter 2nd movie name:")
# c=input("Enter 3rd movie name:")
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)
palin=[1,2,3,4,9,2,1]
copy_palin=palin.copy()
copy_palin.reverse()
if(copy_palin==palin):
    print("palindrome")
else:
    print("not a palindrome")