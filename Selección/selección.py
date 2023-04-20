def selección_corta(lst):
    n = len(lst)
    for i in range(n):
        
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
                
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
    return lst

lst = [53, 21, 43, 36, 11]
lst_ordenada = selección_corta(lst)
print(lst_ordenada)
