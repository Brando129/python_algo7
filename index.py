#Replace any negative list values with 'Dojo'

def replace_negatives(list):

    for i in range(0,len(list)):
        if (list[i] < 0):
            list[i] = 'Dojo'
    return list

print(replace_negatives([2,4,-12,8,-2]))
