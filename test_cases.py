import fuzzy_match
from PIL import Image


def test_case_1():
    path1 = 'images\set1_a.png'
    path2 = 'images\set1_b.png'

    image_1 = Image.open(path1)
    image_2 = Image.open(path2)

    img_str_1 = fuzzy_match.image_2_string(image_1)
    img_str_2 = fuzzy_match.image_2_string(image_2)

    np_array_1 = fuzzy_match.string_2_npArray(img_str_1)
    np_array_2 = fuzzy_match.string_2_npArray(img_str_2)

    res = fuzzy_match.image_fuzzy_match(np_array_1, np_array_2)

    print('test case 1: ', res)

def test_case_2():
    path1 = 'images\set2_a.png'
    path2 = 'images\set2_b.png'

    image_1 = Image.open(path1)
    image_2 = Image.open(path2)

    img_str_1 = fuzzy_match.image_2_string(image_1)
    img_str_2 = fuzzy_match.image_2_string(image_2)

    np_array_1 = fuzzy_match.string_2_npArray(img_str_1)
    np_array_2 = fuzzy_match.string_2_npArray(img_str_2)

    res = fuzzy_match.image_fuzzy_match(np_array_1, np_array_2)

    print('test case 2: ', res)


def test_case_3():
    path1 = 'images\set3_a.png'
    path2 = 'images\set3_b.png'

    image_1 = Image.open(path1)
    image_2 = Image.open(path2)

    img_str_1 = fuzzy_match.image_2_string(image_1)
    img_str_2 = fuzzy_match.image_2_string(image_2)

    np_array_1 = fuzzy_match.string_2_npArray(img_str_1)
    np_array_2 = fuzzy_match.string_2_npArray(img_str_2)

    res = fuzzy_match.image_fuzzy_match(np_array_1, np_array_2)

    print('test case 3: ', res)

def test_case_4():
    path1 = 'images\set1_a.png'
    path2 = 'images\set2_a.png'

    image_1 = Image.open(path1)
    image_2 = Image.open(path2)

    img_str_1 = fuzzy_match.image_2_string(image_1)
    img_str_2 = fuzzy_match.image_2_string(image_2)

    np_array_1 = fuzzy_match.string_2_npArray(img_str_1)
    np_array_2 = fuzzy_match.string_2_npArray(img_str_2)

    res = fuzzy_match.image_fuzzy_match(np_array_1, np_array_2)

    print('test case 4: ', res)



if __name__ == '__main__':

    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
