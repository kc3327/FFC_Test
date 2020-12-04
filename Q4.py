# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 01:59:07 2020

@author: Aaron
"""

class intMappings:
    """
    The intMappings operates all functions for linked nodes
    """
    def __init__(self, mappings={1:2,2:5,5:10,3:12,15:3,6:10}):
        self.mappings=mappings

    def returnAllPaths(self):
        """
        This function returns all paths from the dictionary. The first part of function gives all potential paths. The second part of function eliminates all the subset paths.
        """
        result=[]#create a list to store the final result
        temp=[]#temporarily store the potential path
        tempkey=0#initialize a key
        visited=dict.fromkeys(self.mappings.keys(), False )#a dictionary to check if the key has been visited before
        for key in self.mappings.keys():
            if not visited[key]:# skip if the key has been visited before
                temp.append(key)#append the key to the temp list
                visited[tempkey]=True#mark the key as visited
                tempkey=key
                while tempkey in self.mappings.keys():#loop over the temp key until key not in the keys
                    visited[tempkey]=True#mark the key as visited
                    if self.mappings[tempkey] in temp:#if we find the value is alreay in the temp list
                        raise NameError("Cycle Detected") #raise error
                    temp.append(self.mappings[tempkey])# append the value of the key to the temp list
                    tempkey=self.mappings[tempkey]#replace the key with it value
                result.append(temp)#append the path temp list to the result
                temp=[]#initalize the temp list
        remove_list=[]#create a list to store the list which should be removed in the result, because it is the sublist of another list in the result
        for i in range(len(result)):
            remaining=result[0:i]+result[i+1:]#create a remaining list excluding current element
            current=result[i]#current element
            for ch in remaining:
                if min(set(x in current for x in ch))==True or  min(set(x in ch for x in current))==True:
                    #check if the ch is a subset of current or if the current is a subset of ch
                    if len(ch)>len(current):
                        remove_list.append(current)#append the list with less length(which is a subset of another list)
                    elif len(ch)<len(current):
                        remove_list.append(ch)#append the list with less length(which is a subset of another list)
                    else:
                        pass
        for ch in result.copy():#loop over the result
            if ch in remove_list:#if the element is in the remove list
                result.remove(ch)#remove the element from result
        return result

example=intMappings(mappings={1:2,3:4,5:1,10:5,4:10})
print(example.returnAllPaths())


        
