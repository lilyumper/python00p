"""def odd_even():
    for i in range (1,2000):
        if i % 2 == 1:
            print "Number is",i, "."," ", "This is an odd number."
        if i % 2 == 0:
            print "Number is",i,"."," ", "This is an even number."
odd_even()"""

def multi(arr,num):
    for x in range(len(arr)):
        print x
        arr[x]*= num
    return arr


def layered_multiples(arr):
    newArray = []
    print newArray

    for x in arr:
        newArr =[]
        for i in range (0,x):
            newArr.append(1)
        newArray.append(newArr)
    return newArray
print layered_multiples(multi([2,4,10,16],5))

        
        
    
    