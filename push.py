# A program that conatins functions in a module named push.py
# Lehlogonlo Tshehla
# 08 May 2024

def push_up (grid): 
    """merge grid values upwards"""
    for c in range(4):
        temp = []
        for r in range(4):
            if grid[r][c] != 0:
                temp.append(grid[r][c])
    i = 0
    while i < len(temp)-1:
        if temp[i] == temp[i+1]:
            temp[i] = temp[i]*2
            temp[i+1] = 0
            i+= 0
        i+=1
    
    new = []
    for vv in temp:
        if vv != 0:
            new.append(vv)
    
    while len(new) < 4:
        new.append(0)
    
    for r in range(4):
        grid[r][c] = new[c]     
    
def push_down (grid): 
    """merge grid values downwards"""
    for c in range(4):
        temp = []
        for r in range(4):
            if grid[r][c] != 0:
                temp.append(grid[r][c])
        temp.reverse()
    i = 0
    while i < len(temp)-1:
        if temp[i] == temp[i+1]:
            temp[i] = temp[i]*2
            temp[i+1] = 0
            i+= 0
        i+=1
    
    new = []
    for vv in temp:
        if vv != 0:
            new.append(vv)
    
    while len(new) < 4:
        new.append(0)
    new.reverse()
    
    for r in range(4):
        grid[r][c] = new[c]    

def push_left (grid): 
    """merge grid values left"""
    for r in range(4):
        temp = []
        for c in range(4):
            if grid[r][c] != 0:
                temp.append(grid[r][c])
    i = 0
    while i < len(temp)-1:
        if temp[i] == temp[i+1]:
            temp[i] = temp[i]*2
            temp[i+1] = 0
            i+= 0
        i+=1
    
    new = []
    for vv in temp:
        if vv != 0:
            new.append(vv)
    
    while len(new) < 4:
        new.append(0)
    
    for c in range(4):
        grid[r][c] = new[c]    

def push_right (grid): 
    """merge grid values right"""
    for r in range(4):
        temp = []
        for c in range(4):
            if grid[r][c] != 0:
                temp.append(grid[r][c])
        temp.reverse()
    
    i = 0
    while i < len(temp)-1:
        if temp[i] == temp[i+1]:
            temp[i] = temp[i]*2
            temp[i+1] = 0
            i+= 0
        i+=1
    
    new = []
    for vv in temp:
        if vv != 0:
            new.append(vv)
    
    while len(new) < 4:
        new.append(0)
    new.reverse()
    
    for c in range(4):
        grid[r][c] = new[c]       