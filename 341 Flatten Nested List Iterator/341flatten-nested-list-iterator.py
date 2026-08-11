# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.lists = [nestedList]
        if nestedList:
            self.lists.append(nestedList[0])
        self.indices = [0] if nestedList else []
    
    def next(self) -> int:
        val = self.lists[-1].getInteger()

        # Now that we have accessed the integer, we check if the pointers exceed.
        while self.indices:
            self.indices[-1] += 1 #
            second_last_li = (
                self.lists[-2] if isinstance(self.lists[-2], list) 
                else self.lists[-2].getList()
            )

            if self.indices[-1] < len(second_last_li):
                self.lists.pop()
                self.lists.append(second_last_li[self.indices[-1]])
                break
            
            self.indices.pop()
            self.lists.pop()
            
        return val
    
    def hasNext(self) -> bool:
        if not self.indices:
            return False
        
        # Tidy up
        # First, check if the last element is a nested list that we can go into
        while not self.lists[-1].isInteger():
            li = self.lists[-1].getList()
            if li:
                self.indices.append(0)
                self.lists.append(li[0])
            else:
                while self.indices:
                    self.indices[-1] += 1 #
                    second_last_li = (
                        self.lists[-2] if isinstance(self.lists[-2], list) 
                        else self.lists[-2].getList()
                    )

                    if self.indices[-1] < len(second_last_li):
                        self.lists.pop()
                        self.lists.append(second_last_li[self.indices[-1]])
                        break
                    
                    self.indices.pop()
                    self.lists.pop()
                
                if isinstance(self.lists[-1], list):
                    return False

        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())