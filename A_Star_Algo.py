#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import product

class node:    
    def __init__(self, node_co_orinate, node_gScore,node_hScore):        
        self.coOrd = node_co_orinate       
        self.gScore = node_gScore
        self.hScore = node_hScore
        self.parent = None
    def fScore(self):
        return self.gScore + self.hScore
    def setparent(self,parent):
        self.parent = parent

def h_score(a, b):
    import math
    return math.sqrt((b[0] - a[0])**2  + (b[1] - a[1])**2)

def a_star(array, start, goal):
    
    OpenSet = []
    ClosedSet = set()
    
    start_node = node(start,0,999999999)
    
    OpenSet.append(start_node)
    
    while OpenSet:        
        OpenSet = sorted(OpenSet,key = lambda ele: ele.fScore(),reverse = True)
        current = OpenSet.pop()
        ClosedSet.add(current.coOrd)
                
        if current.coOrd == goal:
            path = []
            while current:                
                path.append(current.coOrd)                
                current = current.parent
            
            return path[::-1]
        
        for neighbour in list(product([0,1,-1], repeat =2)):            
            neighbour_coOrd = (current.coOrd[0]+neighbour[0],current.coOrd[1]+neighbour[1])
            neighbour_gScore = current.gScore + 0
            
            valid_coOrd = True if 0<neighbour_coOrd[0]<array.shape[0] and 0<neighbour_coOrd[1]<array.shape[1] else False
                        
            if not valid_coOrd or array[neighbour_coOrd] == 1 or neighbour_coOrd in ClosedSet:
                continue
            if not neighbour_coOrd in list(map(lambda n:n.coOrd,OpenSet)) and valid_coOrd:
                neighbour_hScore = h_score(neighbour_coOrd,goal)
                neighbour_node = node(neighbour_coOrd,neighbour_gScore,neighbour_hScore)
                neighbour_node.setparent(current)
                OpenSet.append(neighbour_node)
    return False
        


# In[2]:


import numpy as np
plot = np.array([
       [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
       [0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
       [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0],
       [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1],
       [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0],
       [0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1]])


# In[4]:


print(a_star(plot,(19,12),(18,17))) 


# In[ ]:




