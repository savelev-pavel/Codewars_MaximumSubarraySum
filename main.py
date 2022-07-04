"""
https://www.codewars.com
Maximum subarray sum
"""
def max_sequence(arr):
    result = 0
    arrHasNegative = False
    arrHasPositive = False
    for i in arr:
        if i > 0: arrHasPositive = True
        elif i < 0: arrHasNegative = True
        result += i
    if arrHasPositive and not arrHasNegative:
        return result
    elif not arrHasPositive:
        return 0
    else:
        result = 0
        for j in range(len(arr),0,-1):
            for i, _ in enumerate(arr[:j]):
                sum = 0
                for val in arr[i-1:j]:
                    sum += val
                    if sum > result:
                        result = sum
        return result