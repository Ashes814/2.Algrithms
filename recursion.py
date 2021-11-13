list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 3, 4, 5,8,8,8]


# 递归对列表求和
def sum_4_1(arr):
    if len(arr) == 0:
        return 0
    else:

        result = arr[0] + sum_4_1(arr[1:])
    return result


print(sum_4_1(list1))


# 递归求列表长度
def find_length(list):
    if list == []:
        return 0
    return 1 + find_length(list[1:])


print(find_length(list1))


# 递归求list最大值

def find_max(list):
    if find_length(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    return list[0] if list[0] > find_max(list[1:]) else find_max(list[1:])

print(find_max(list2))