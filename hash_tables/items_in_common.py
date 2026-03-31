def item_in_common(list1, list2):
    items = {}
    for item in list1:
        items[item] = True
    for item in list2:
        if item in items:
            return True
    return False

print(item_in_common([1, 2, 3], [6, 4, 5]))