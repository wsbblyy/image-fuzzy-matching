import imagehash, numpy


def image_2_string(image):
    hash = imagehash.average_hash(image)
    np_array = hash.hash.flatten().tolist()
    return ''.join(['1' if x else '0' for x in np_array])

def string_2_npArray(string):
    return numpy.array([True if x =='1' else '0' for x in string])
    


    
def image_fuzzy_match(np_array1, np_array2):
    return numpy.count_nonzero(np_array1 != np_array2)