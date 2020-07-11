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


storge_block=[(1,8),(2,7),(9,1)]
'''
x=2
y=1
one_block=[(-1,-1),(0,-1),(-1,0),(0,0)]
for x1,y1 in one_block:
    dirction=[0,0]
    x2=x+x1
    y2=y+y1
    #print(x1,y1)
    #print(x2,y2)
    #print("\n")
    while True:
        if (x2,y2) not in storge_block:
            #print(x2,y2)
            print(type(dirction[1]))
            dirction[1]= dirction[1]+1
            y2=y+y1+dirction[1]
        else:
            break
print(x2,y2)
print(dirction)
'''
print(storge_block[1][0])
storge_block[1]=(2,0)
print(storge_block)

       
            