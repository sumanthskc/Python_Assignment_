class ReverseIter:
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.data[self.index]
try:
    my_list=[1,2,3,4,5,6]
    reverseItr=ReverseIter(my_list)
    myiter=iter(reverseItr)

    for x in myiter:
        print(x)
    print(next(myiter))
except StopIteration:
    print("Exception to stop iteration")



    