"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""

def snail(snail_map):
    result = []
    while snail_map:

        result += snail_map.pop(0)

        for i in snail_map:
            if i:
                result.append(i.pop(-1))

        if snail_map:
            result += snail_map.pop(-1)[::-1]

        for i in reversed(snail_map):
            if i:
                result.append(i.pop(0))
        
    return result



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    
print(snail(array)) #expected = [1,2,3,6,9,8,7,4,5]    