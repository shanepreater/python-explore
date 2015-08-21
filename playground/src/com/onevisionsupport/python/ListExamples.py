'''
Created on 12 Aug 2015

List playground.

@author: Shane Preater
'''

class ListPlayground:
    '''
    Simple class to hold some methods which manipulate the lists in various ways.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def printAll(self, items):
        for item in items:
            print(item, end=" ")
        print("")
    
    def reverseAList(self):
        myList = [0,1,2,3,4,5,6,7,8]
        print("Initial list: ")
        self.printAll(myList)
        
        
        #Now use the comprehension to revrse it
        reversedByComprehension = [8 - num for num in myList]
        print("Reversed by comprehension: ")
        self.printAll(reversedByComprehension)
        
        reversedByComprehension.reverse()
        print("Reversed using method")
        self.printAll(reversedByComprehension)

    def sortingAndShuffling(self):
        myList = ['I', 'was', 'here']
        print("Add a new item to the end: ")
        myList.append('today')
        self.printAll(myList)
        
        print("Insert a new item at the start")
        myList.insert(0, "And")
        self.printAll(myList)
        
        print("Queue (FIFO) style removal")
        myList.pop(0)
        self.printAll(myList)
        
        print("Stack (LIFO) behaviour")
        myList.append("NOW")
        self.printAll(myList)
        myList.pop()
        self.printAll(myList)
        
        print("sort our list")
        alpha = myList
        alpha.sort()
        self.printAll(alpha)
        alpha.sort(reverse=True)
        
        print("Descending")
        self.printAll(alpha)
        
        print("Remove the odds")
        splitItems = [item for item in alpha if alpha.index(item) % 2 != 0]
        self.printAll(splitItems)
        
        print("Remove every third item")
        splitItems = [item for item in alpha if alpha.index(item) % 3 != 0 or alpha.index(item) == 0]
        self.printAll(splitItems)
        
        
playground = ListPlayground()
playground.reverseAList()
playground.sortingAndShuffling()