def hanoi(n, source, target, auxiliary):
    if n > 0:        
        hanoi(n - 1, source, auxiliary, target)     
        print('%s  %s' % ( source, target))        
        hanoi(n - 1, auxiliary, target, source)

hanoi(2, 1, 3, 2)
