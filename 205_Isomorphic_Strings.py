'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(c) for c in s] == [t.index(c) for c in t]
'''


s1 = "egg"
s2 = "add"

l1 = len(s1)
l2 = len(s2)

map1 = {}
map2 = {}

if l1 != l2:
     print ("Strings have different lengths")
    
else:
    for i in range(l1):
        c1 = s1[i]
        c2 = s2[i]
        
        if c1 in map1 and map1[c1] != c2:
            print("False")
            break
        
        if c2 in map2 and map2[c2] !=c1:
            print("False")
            break
        
        map1[c1] = c2
        map2[c2] = c1
        
    else:
        print(True)
        
        



    