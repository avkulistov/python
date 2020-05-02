
def quick_sort(unsort_list):
    if len(unsort_list) < 2:
        return unsort_list

    less_list = []
    more_list = []
    sup_elem = unsort_list[0]
    for num in unsort_list[1:]:
        if num <= sup_elem:
            less_list.append(num)
        else:
            more_list.append(num)
    return quick_sort(less_list) + [sup_elem] + quick_sort(more_list)


test_list = [7, 3, 8, 43, 7, 9879, 54, 22, 6]
print(quick_sort(test_list))
