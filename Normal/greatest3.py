
def greatest():

    n=(input("enter 3 numbers"))

    a = n.split()

    nums = [int(i) for i in a]

    greatest = nums[0]

    for b in range(1,len(nums)):
        if nums[b] > greatest:
            greatest = nums[b]
    return greatest
   
    
highest = greatest()
print("greatest number is ", highest)

        # [4,6,2]
    



    # if u want to access the list then make i as value but if u want to access the list and index and then make i as a number
