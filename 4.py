import numpy as np
array_3d=np.zeros((3,5,8),dtype=int)
print(array_3d)
another_3d=[[[0 for _ in range(8)] for _ in range(5)]for _ in range(3)]
for i in another_3d:
    for j in i:
        for k in j:
            print(k,end=" ")
        print( )
    print(" \n")
