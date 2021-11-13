def sum_4_1(arr):
    if len(arr) == 0:
        return 0
    else:

        result = arr[0] + sum_4_1(arr[1:])
    return result


print(sum_4_1([1, 2, 3, 4, 5,24,24,224,24,24]))


#addffffff
#####