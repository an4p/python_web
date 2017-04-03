def mmin(arr, first_index, second_index):
    if first_index >= len(arr):
        return second_index
    if second_index >= len(arr):
        return first_index
    if arr[first_index] > arr[second_index]:
        return second_index
    else:
        return first_index

def hapify(arr, index_min, last):
    while index_min < len(arr):
        left_child = 2*index_min + 1
        right_child = 2*index_min + 2
        if left_child >= last and right_child >= last:
            break
        index = mmin(arr, left_child, right_child)
        if arr[index_min]>arr[index]:
            arr[index_min], arr[index] = arr[index], arr[index_min]
            index_min = index
        else:
            break

def create_pyramyde(arr):
    last = len(arr) - 1
    if len(arr)%2 == 0:
        parent = (last - 1)//2
        if arr[parent] > arr[last]:
            arr[parent],arr[last] = arr[last], arr[parent]
            last = last - 1
    while last > 0:
        parent = (last - 1)//2
        index_min = mmin(arr, last, last - 1)
        # print(last, last - 1, index_min, parent)
        if arr[parent] > arr[index_min]:
            arr[parent], arr[index_min] = arr[index_min], arr[parent]
            # print(arr)
            hapify(arr, index_min, len(arr))
         # print(arr)
        last = last - 2

def sort_arr(arr):
    create_pyramyde(arr)
    last = len(arr) - 1
    while last > 1:
        # print(last)
        # print(arr)
        arr[0], arr[last] = arr[last], arr[0]
        last = last - 1
        hapify(arr, 0, last)










arr = [30, 8, 16, 24, 5, 18, 29, 14, 1]
print(arr)
sort_arr(arr)
print(arr)