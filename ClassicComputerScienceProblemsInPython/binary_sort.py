def binary_sort(search_list: list, item: str) -> bool:
    center_elem_index: int = len(search_list) // 2
    result: bool = False
    if len(search_list) == 0:
        return False
    if item == search_list[center_elem_index]:
        result = True
    elif item < search_list[center_elem_index]:
        result = binary_sort(search_list[0: center_elem_index], item)
    elif item > search_list[center_elem_index]:
        result = binary_sort(search_list[center_elem_index: len(search_list)], item)

    return result


def binary_sort_iter(search_list: list, item: str) -> bool:
    low: int = 0
    high: int = len(search_list) - 1
    while low < high:
        mid:int (low + high) // 2
        if search_list[mid] == item:
            return True
        elif search_list[mid] < item:
            low = mid + 1
        elif search_list[mid] > item:
            high = mid - 1

    return False


if __name__ == "__main__":
    test_list = ['заяц', 'зебра', 'кенгуру', 'кошка', 'крыса', 'лама', 'собака']

    print(binary_sort(test_list, 'gbcz'))
