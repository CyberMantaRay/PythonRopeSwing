# Author @AndorLight

import math;

#######################
###     STRINGS     ###
#######################                 # A=65, Z=90, a=97, z=122

def swap(num_string):
    r"""Swap commas/periods in given numerical string, e.g. "1,234.56" → "1.234,56"
    """
    result=[]

    for char in num_string:
        match char:
            case ',':
                result.append('.')
            case '.':
                result.append(',')
            case _:
                result.append(char)
    return "".join(result)

def swap_case(string):
    r"""Swap cases in given string, e.g. "SpiRit" → "sPIrIT"
    """
    val=0
    result=[]

    for char in string:
        val=ord(char)

        if val > 64 and val < 91:
            result.append(chr(val+32))
        elif val > 96 and val < 123:
            result.append(chr(val-32))
        else:
            result.append(char)
    return "".join(result)

# print(swap("23,450.32"))
# print(swap("32.238.054,23"))
# print(swap_case("SpiRit WoRLd"))


#######################
###      LOOPS      ###
#######################

def arrow_pattern(rows):
    r""" Return an arrow pattern constructed with "* " given number of rows
    """
    if(rows < 3): return

    IS_ROW_COUNT_ODD = rows%2==1
    MID = rows//2 if IS_ROW_COUNT_ODD else rows//2-1

    for i in range(rows):
        if i <= MID:
            print("* " * (i+1))
        else:
            print("* " * (rows-i))
    print()

def vowel_or_consonant(char):
    if len(char) != 1: return
    val=ord(char)
    if val < 65 or val > 122 or (val > 90 and val < 97): return 

    match char:
        case 'A' | 'E' | 'I' | 'O' | 'U' | 'a' | 'e' | 'i' | 'o' | 'u':
            return f"{char} is a vowel."
        case _:
            return f"{char} is a consonant."

def median(arr):
    r"""Find the median of numerical array
    """
    arr.sort()                      # Sort array in-place; sorted(arr) for copy

    if len(arr)%2==1:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2-1] + arr[len(arr)//2])/2

# arrow_pattern(3)
# arrow_pattern(6)
# arrow_pattern(9)
# print(vowel_or_consonant('I'))
# print(vowel_or_consonant('u'))
# print(vowel_or_consonant('X'))
# print(median([5,1,3,9,7]))
# print(median([8,2,6,4]))


#######################
###      LISTS      ###
#######################

def process_arr_for_strings(arr):
    result=0
    for ele in arr:
        if(isinstance(ele, str) and len(ele)>2 and ele[0]==ele[len(ele)-1]):
            result+=1
    return result

def integer_frequency(arr):
    freq={}
    for num in arr:
        if(freq.get(num)): freq[num] += 1
        else: freq[num] = 1
    
    for i, (k, v) in enumerate(freq.items()):
        if i+1 < freq.__len__():
            print(f"{k}:{v}", end=", ")
        else: print(f"{k}:{v}")

# print(process_arr_for_strings([4,2,"ruffnut", "tuffnut"]))
# print(process_arr_for_strings(["bob", "racecar", "sponge"]))
# print(process_arr_for_strings(["1a2b3c", "tacocat"]))
# integer_frequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30])


#######################
###    FUNCTIONS    ###
#######################

def get_max(*args):
    result = -math.inf
    for num in args:
        if num > result: result = num
    return result

# def reverse_words(string):
#     arr = str(string).upper().split()
#     arr.reverse()
#     return (" ").join(arr)

def reverse_words(string):
    arr = str(string).upper().split()[::-1]
    return (" ").join(arr)

# print(get_max(39,27,42,18,55,24,86,12))
# print(reverse_words("Who knocks at the garden gate"))


############################
###     DICTIONARIES     ###
############################

def combine_dict(*dictionaries: dict):
    result = {}
    for dict in dictionaries:
        result |= dict
    return result

def combine_add(*dictionaries: dict):
    if len(dictionaries) != 2: return
    result = dictionaries[0]
    for k,v in dictionaries[1].items():
        if k in result:
            result[k] += v
        else: result[k] = v
    return result


def sort_dict_by_values(x: dict):
    return list({k: v for k, v in sorted(x.items(), key=lambda entry: entry[1])})

# print(combine_dict({82: "aang", 83: "korra"}, {81: "roku", 1: "wan", 80: "kyoshi"}, {79: "kuruk", 78: "yangchen"}))
# print(combine_add({'e': 75, 'w': 175, 'f':340}, {'e': 225, 'w': 250, 'a':525}))
# print(sort_dict_by_values({39:42, 38:9, 46:10, 41:19, 1:17, 7:25, 20:16}))
