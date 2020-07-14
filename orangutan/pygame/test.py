'''
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

storge_block=[[0 for i in range(12)]for i in range20)]
for i in range(20):
    print(storge_block[i])
    '''


full_row_list=[19,20,8]
full_row_list.sort(reverse=False)
print (full_row_list)
while full_row_list:
    max_row=max(full_row_list)
    for i in range(max_row,0,-1):
        print(i)
        for j in range(12):
            print(i,j)
    full_row_list.pop()
    print(full_row_list)
