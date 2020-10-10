"""
Implement the RandomizedSet class:
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?
"""
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.set.__contains__(val):
            return False
        else:
            self.set.add(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.set.__contains__(val):
            self.set.remove(val)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        n = len(self.set)
        if n == 0:
            return False
        else:
            g = self.set.pop()
            self.set.add(g)
            return g
        

# sets = set()
# sets.add(1)
# sets.add(2)
# print(sets)
# sets.remove(1)
# print(sets)
# print(sets.)
# obj = 
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj)
param_1 = obj.insert(1)
print(param_1)
param_2 = obj.remove(2)
print(param_2)
param_3 = obj.insert(2)
print(param_3)
param_3 = obj.getRandom()
print(param_3)
param_4 = obj.remove(1)
print(param_4)
param_5 = obj.getRandom()
print(param_5)