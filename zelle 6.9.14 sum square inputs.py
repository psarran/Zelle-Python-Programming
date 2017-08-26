#zelle 6.9.14

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

def sumList(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def main():
    fname = input('enter filename: ')
    infile = open(fname, 'r')
    nums = infile.readlines()

    print(sumList(squareEach(toNumbers(nums))))

    infile.close()

main()
    
