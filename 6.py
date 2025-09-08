# #6. Write a program using generator to print the numbers which can be divisible by 5 
# and 7 between 0 and n in comma separated form while n is input by console.  

def generator(end):
    for i in range(end+1):
        if i%5 ==0 and i%7 ==0:
            yield i
end=int(input("Enter a number: "))
result=list(str(ele) for ele in generator(end))
print(",".join(result))

#or

# res=list(generator(end))
# for ele in res:
#     print(f"{ele}",end=",")
# print()