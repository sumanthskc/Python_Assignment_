import os
import sys
def print_tree(path,indent="->"):
    for item in os.listdir(path):
        full_path=os.path.join(path,item)
        print(indent+item)
        if os.path.isdir(full_path):
            print_tree(full_path,indent+"-->")
root=sys.argv[1]

print(root)
print_tree(root)
        