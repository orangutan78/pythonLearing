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

storge_block=[[0 for i in range(12)]for i in range(20)]
storge_block[2][1]=1
for i in range(20):
    print(storge_block[i])