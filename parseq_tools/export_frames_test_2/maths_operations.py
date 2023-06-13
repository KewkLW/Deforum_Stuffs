from math import degrees
from math import isclose

def roundZero(num, magnitude_thresh = 0.00001):
    if abs(num) > magnitude_thresh:
        return num
    else:
        return 0
        
def arr_to_keyframes(arr):
    keyframes = ""
    for i, val in enumerate(arr):
        val = roundZero(val)
        last_is_same = i > 0 and isclose(val, roundZero(arr[i-1]))
        next_is_same = (i+1) < len(arr) and isclose(val, roundZero(arr[i+1]))        
        omit = last_is_same and next_is_same        
        if not omit:
            keyframes += f"{i}:({val}),"
    return keyframes
