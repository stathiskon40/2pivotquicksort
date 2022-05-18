def QuickSort2Pivot(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2:
        return sorted(list)

    pivot1, pivot2 = sorted([list.pop(0), list.pop(0)])

    a = []
    b = []
    c = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        else:
            c.append(element)

    return QuickSort2Pivot(a) + [pivot1] + QuickSort2Pivot(b) + [pivot2] + QuickSort2Pivot(c)
