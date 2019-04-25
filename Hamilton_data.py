"""
get data from a polygon description.
"""
def sommets_depuis_un_point(name):
    """
    Return : a dic where like  {a point: [reacheable points from this point]}
    """
    s = open('polys/'+name,"r")
    dic = {}
    k = 0
    for i in range(3):
        f = s.readline().split()
    for i in range(int(f[0])+int(f[1])):
        s.readline()
    for i in range(int(f[2])):
        k = [int(i) for i in s.readline().split()]
        if k[0] not in dic:
            dic[k[0]] = [k[1]]
        elif k[1] not in dic[k[0]]:
            dic[k[0]].append(k[1])    
        if k[1] not in dic:
            dic[k[1]] = [k[0]]
        elif k[0] not in dic[k[1]]:
            dic[k[1]].append(k[0])  
    return dic
def sommets_unilateral(name):
    s = open('polys/'+name,"r")
    dic = {}
    k = 0
    for i in range(3):
        f = s.readline().split()
    for i in range(int(f[0])+int(f[1])):
        s.readline()
    for i in range(int(f[2])):
        k = [int(i) for i in s.readline().split()]
        if k[0] not in dic:
            dic[k[0]] = [k[1]]
        elif k[1] not in dic[k[0]]:
            dic[k[0]].append(k[1])    
         
    return dic        
        
