# calculate positive number count from a list
# numbers=[1,-2,-4,4,5,6,7,-9]
# positive_number_count=0
# for n in numbers:
#     if n>0:
#         positive_number_count+=1
#         print(f"positive numbers is: {n} ")
# print(f"Total count of positive number is: {positive_number_count}")


#sum of even numbers
# n=int(input("Enter number: "))
# even_count=0
# sum_even=0
# for i in range(1,n+1):
#     if i%2==0:
#         even_count+=1
#         sum_even+=i
#         # print(i+i)
# print("sum of even numbers till n is: ",sum_even)
# print("count of even numbers till n is: ",even_count)

#print table of a number and skip fifth iteration
# number=int(input("Enter number whose table you want to print: "))
# for i in range(1,11):
#     if i==5:
#         continue
#     print(number,"x",i,"=",number*i)

# reverse a string using loop
# input_str="Software"
# reverse_str=""
# for char in input_str:
#     reverse_str=char + reverse_str
# print(reverse_str)

# fist non-repeated character in a string
# input_string="sweetpatatos"
# for char in input_string:
#     if input_string.count(char)==1:
#         print("Char is: ",char)
#         break

# factorial using while loop
# number=5
# factorial=1
# while number > 0:
#     factorial=factorial*number
#     number=number-1
# print("factorial is: ",factorial)

# prime number
# number=29
# is_prime=True
# if number > 1:
#     for i in range(2,number):
#         if number%2==0:
#             is_prime=False
#             print("Not a prime number")
#             break
# print(is_prime)

#duplicate item in a list
items=['apple','mango','banana']
for item in items:
    if items.count(item)>1:
        print("duplicate detected: ",item)
        break
print("No duplication")








