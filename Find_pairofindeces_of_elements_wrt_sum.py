"""
Finding the indeces of two numbers on a list which sums to a certain number
Tip: 1) Don't change anything with the numbers
     2) Only play with the indexes
"""
def find_two_sum(numbers, targetsum):
    allrange = list(range(len(numbers))) #list of the indexes for the number list
    result = list() #a list to store the pair of indexes

    for i in allrange:
        exceptlist = allrange[:i]+allrange[i+1:] #all indexes in the list except index i
        #print(exceptlist)
        for j in exceptlist:
            if numbers[i] + numbers[j] == targetsum:
                result.append([i,j])
    print("Pair of indeces of elements which sum is the targetsum are:",result)

numbers = [3, 1, 5, 7, 5, 9]
targetsum = 10
find_two_sum(numbers,targetsum)
