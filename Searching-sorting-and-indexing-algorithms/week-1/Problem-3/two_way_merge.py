def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on two ascending order sorted lists
    # return a fresh ascending order sorted list that merges lst1 and lst2
    i,j = 0,0
    result_list = []
    
    while i<len(lst1) and j<len(lst2):
        
        if lst1[i] < lst2[j]:
            result_list.append(lst1[i])
            i+=1
        else:
            result_list.append(lst2[j])
            j+=1
        
    result_list = result_list + lst1[i:] + lst2[j:]
    return result_list

# given a list_of_lists as input, 
#   if list_of_lists has 2 or more lists,  compute 2 way merge on elements i, i+1 for i = 0, 2, ...
#   return new list of lists after the merge
#   Handle the case when the list size is odd carefully.
def oneStepKWayMerge(list_of_lists):
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    for i in range(0, k, 2):
        if (i < k-1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i+1]))
        else: 
            ret_list_of_lists.append(list_of_lists[k-1])
    return ret_list_of_lists

def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)