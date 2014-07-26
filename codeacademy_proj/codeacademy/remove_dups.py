__author__ = 'rushil'

def remove_duplicates(lst):
    no_dups = []
    for index, item in enumerate(lst):
        is_dup = False
        for j in range(index+1, len(lst)):
            if item == lst[j]:
                is_dup = True
        if is_dup == False:
            no_dups.append(item)

    return no_dups

print remove_duplicates([1,1,2,2,3])
print remove_duplicates([1])