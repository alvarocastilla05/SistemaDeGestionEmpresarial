def comparacion_arrays(array1, array2, boolean):
    result = []
    if boolean:
        for item in array1:
            if item in array2 and item not in result:
                result.append(item)
    else:
        for item in array1:
            if item not in array2 and item not in result:
                result.append(item)
            for item in array2:
                if item not in array1 and item not in result:
                    result.append(item)
    return result

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

print(comparacion_arrays(array1, array2, True)) 

print(comparacion_arrays(array1, array2, False))  
