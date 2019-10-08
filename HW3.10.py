
"""
Author: Sam Bluestone
Math 321 HW 3.10
Determines if Un (all of the postive integers strictly less than n that are relatively prime to n) is cyclic for any value n
"""


n = [ 5, 9, 10, 14, 15, 18, 20, 22, 25, 8, 16];

def main():

    for x in n:
        #prints Un, generators of Un, and whether or not Un is cyclic
        #Note: Un is cyclic if it has a generator
        print("U(%d): %s\nGenerators of U(%d): %s\nCyclic: %s\n"% (x, Un(x), x, getGenerators(Un(x), x), not(getGenerators(Un(x), x) == [])))
    

""" Determines if x and y are coprime to each other"""
def isCoPrime(x, y):
    lcm = 1
    num = min(x, y)
        
    for i in range(num, 1, -1):

        if x % i == 0 and y % i == 0:
            lcm = i

    return lcm == 1
        

"""Returns the set of postive integers that are
    elatively prime to a given positive integer  """
def Un(num):
    Un = []
    for x in range(1, num):
        if isCoPrime(x, num):
            Un.append(x)

    return Un

"""Returns the generators of a set Un""""
def getGenerators(Un, length):
    generators = []
    for a in Un:
        if isGenerator(Un,length,  a):
            generators.append(a)

    return generators


"""Determines if an element a is a generator of Un """
def isGenerator(Un, length,  a):

    nums = []    
    pNum = 1
    for x in range(len(Un)):
        nums.append((a * pNum) % length)
        pNum *= a
 
    list.sort(nums)

    return nums == Un




if __name__ == "__main__":
    main()
