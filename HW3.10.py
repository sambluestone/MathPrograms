



n = [ 5, 9, 10, 14, 15, 18, 20, 22, 25, 8, 16];

def main():

    for x in n:
        print("U(%d): %s\nGenerators of U(%d): %s\nCyclic: %s\n"% (x, Un(x), x, getGenerators(Un(x), x), not(getGenerators(Un(x), x) == [])))
    

def isCoPrime(x, y):
    lcm = 1
    num = min(x, y)
        
    for i in range(num, 1, -1):

        if x % i == 0 and y % i == 0:
            lcm = i

    return lcm == 1
        

def Un(num):
    Un = []
    for x in range(1, num):
        if isCoPrime(x, num):
            Un.append(x)

    return Un

def getGenerators(Un, length):
    generators = []
    for a in Un:
        if isGenerator(Un,length,  a):
            generators.append(a)

    return generators


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
