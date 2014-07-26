__author__ = 'rushil'
def median(lst):
    lst.sort()
    index = len(lst)/2
    if len(lst) % 2 == 0:
        mid1 = lst[index]
        mid2 = lst[index-1]
        return (mid1+mid2)/2.0
    else:
        return lst[index]

print median([4,5,5,4])