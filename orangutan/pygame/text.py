block_list={"O":{"pos":[(-1,-1),(0,-1),(-1,0),(0,0)],"color":"blue"},
                "L":{"pos":[(0,-2),(0,-1),(0,0),(1,0)],"color":"red"},
                "J":{"pos":[(0,-2),(0,-1),(0,0),(-1,0)],"color":"orange"},
                "I":{"pos":[(0,-2),(0,-1),(0,0),(0,1)],"color":"pink"},
                "S":{"pos":[(1,-1),(0,-1),(0,0),(-1,0)],"color":"green"},
                "Z":{"pos":[(-1,-1),(0,-1),(0,0),(1,0)],"color":"brown"},
                "T":{"pos":[(-1,0),(0,0),(1,0),(0,1)],"color":"cyan"},
    }
#print(block_list.keys())
#print(list(block_list.keys()))


dic=[(1,0),(1,0),(1,1)]

x=0
y=0
print((x,y) in dic)
if (x,y) in dic:
   print(dic)