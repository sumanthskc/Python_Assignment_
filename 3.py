my_list=eval(input("Enter a list [] :: "))
removed_dup=[]
non_dup=set()

for ele in my_list:
    if ele not in removed_dup:
        non_dup.add(ele)
        removed_dup.append(ele)
removed_dup.reverse()
print(f"Duplicate remove in reverse order:: {removed_dup}")