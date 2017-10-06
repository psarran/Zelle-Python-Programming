#zelle 11.9.5 list operations

from random import randrange

def count(mylist, x):
    """ count the occurences of x in mylist """
    count = 0
    for i in mylist:
        if i == x:
            count += 1
    return count

def isin(mylist, x):
    """ return True if x is an item in mylist, otherwise return False """
    return count(mylist, x) > 0

def index(mylist, x):
    """ return the index of the first occurence of x in mylist
        returns error if x does not occur in mylist
    """
    counter = 0 #to keep track of current index as we loop thru
    tracker = 0 #how many times x has been found in mylist as we loop thru
    for i in mylist:
        if i == x:
            tracker +=1
            if tracker == 1: #only save the current index position of the first occurence
                ans = counter
        counter += 1
    return ans

def reverse(mylist):
    """" reverse the order of mylist items """
    newlist = []
    i = len(mylist) - 1
    while i >=0:
        newlist.append(mylist[i])
        i -= 1
    return newlist

def sort(mylist):
    """ sorts the items in mylist
        returns error if mylist includes non-numeric items
    """
    sortedlist = []
    i = 0
    while i < len(mylist):
        j = 0
        while j <= len(sortedlist):
            if j == len(sortedlist) or mylist[i] <= sortedlist[j]:
                #loops through the sortedlist stopping either at the end or the first time it
                #reaches an element of sortedlist less than the current element of mylist
                #the check for end of list has to be first in the 'or' statement because
                #it will throw an index error in sortedlist[j]
                sortedlist.insert(j, mylist[i])
                break
            j += 1
        i += 1
    return sortedlist

def shuffle(mylist):
    shuffledlist = []
    shuffledlist.append(mylist[0])
    i=1
    while i < len(mylist):
        j = randrange(len(shuffledlist))
        shuffledlist.insert(j, mylist[i])
        i+=1
    return shuffledlist

def innerproduct(x,y):
    # x and y must be the same length
    i = 0
    product = 0
    while i < len(x):
        product += x[i] * y[i]
        i += 1
    return product 
    
def test():
    x = [1, 4, 2, 5, 3, 6, 'a', 'b', 'a', 'c', 2, 2, 2]
    y = [10, 6, 4, 2, 3, 5, 3, 4, 1, 10]
    print('count test:', count(x, 'a'), count(y, 3))
    print('isin test:', isin(x, 'a'), isin(x, 'd'), isin(y, 2.5))
    print('index test:', index(x, 'a'), index(x, 2), index(y, 3))
    print('sort test:',sort(y))
    print('shuffle test:', shuffle(x), shuffle(x), shuffle(x))
    print('innerproduct test:', innerproduct([1,2,3,4], [4,6,8,10]))
    
if __name__ == '__main__': test()
#if __name__ == '__main__': main()
