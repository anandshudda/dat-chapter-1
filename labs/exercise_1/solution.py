def return33( numbers ):
    
    sublist = []
    
    for n in numbers:
        
        if (n % 33) == 0:
            sublist.append(n)
    
    
    return sublist

print return33( [13, 33, 34, 45] )