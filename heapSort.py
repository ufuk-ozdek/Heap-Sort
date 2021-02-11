def max_heapify(arr, index):
    if 2*(index+1) <= len(arr):
        if 2 * (index + 1) + 1 <= len(arr):
            if arr[index] < arr[2 * (index+1)-1] and arr[2 * (index+1)] < arr[2 * (index+1)-1]:
                arr[index], arr[2 * (index+1)-1] = arr[2 * (index+1)-1],  arr[index]
                return max_heapify(arr, 2 * (index + 1) - 1)
            if arr[index] < arr[2 * (index+1)] and arr[2 * (index+1)] > arr[2 * (index+1)-1]:
                arr[index], arr[2 * (index+1)] = arr[2 * (index+1)],  arr[index]
                return max_heapify(arr, 2*(index+1))

        else:
            if arr[index] < arr[2 * (index+1)-1]:
                arr[index], arr[2 * (index + 1) - 1] = arr[2 * (index + 1) - 1], arr[index]
                return max_heapify(arr, 2*(index+1)-1)
    else:
        return arr


def heap_sort(arr):
    # making max heap
    length = len(arr)
    x = length // 2
    for i in range(x, 0, -1):
        max_heapify(arr, i-1)
    # getting max every time
    list_0 = []
    for i in range(len(arr)):
        list_0.append(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        max_heapify(arr, 0)
    return list_0


print(heap_sort(list_1))
