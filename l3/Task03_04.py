list = ['a', 's', 6, 12, 'a', 8, '8', 8, 12, 'a', 12, ['a', 's', 12], 's', 's', 3, ['a', 's', 12]]

def sort_list(list):
    new_list = []
    for i in range(len(list)):
        cur_list = []
        for element in list:
            if list.count(element) == i and not cur_list.count(element):
                cur_list.append(element)
        if cur_list: new_list.append(cur_list)
    return new_list

print(sort_list(list))


