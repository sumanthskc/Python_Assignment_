def binary_serach(sorted_list,target):
    low=0
    high=len(sorted_list)-1
    
    while low<=high :
        mid = (low+high) // 2
        if sorted_list[mid]==target:
            return mid
        elif sorted_list[mid]<target:
            low=mid+1
        else:
            high= mid -1 
            
    return -1

unsorted_list=eval(input("Enter a list "))
target=int(input("Enter target ele"))
(unsorted_list).sort()
sorted_list=unsorted_list

result=binary_serach(sorted_list,target)
if result==-1:
    print("Not found")
else:
    print(f"{target} found at {result}")