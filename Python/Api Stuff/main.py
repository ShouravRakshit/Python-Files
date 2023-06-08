def highest_even(li):
    result = li[0]
    for items in li:
        if items > result and items % 2 == 0:
            result = items

    return result


print(highest_even([10, 20, 3, 4, 8, 11]))
