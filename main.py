"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        val = foo(x - 1) + foo(x - 2)
        return val

def longest_run(mylist, key):
    maxCount =0
    count =1
    index =0
    if key in mylist:
        while index < len(mylist) -1:
            if mylist[index] == key and mylist[index] == mylist[index + 1]:
                count += 1
            else:
                if (count > maxCount):
                    maxCount = count
                count = 1
            index += 1
    else:
        return 0

    if(count>maxCount):
        maxCount=count
    print(maxCount)
    return maxCount


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_rec(mylist, key, start, end,res):
    if start == end:
        return 1 if mylist[start] == key else 0

    mid = (start + end) // 2
    left_length = longest_run_rec(mylist, key, start, mid,res)
    right_length = longest_run_rec(mylist, key, mid + 1, end,res)
    left_count = 0
    for i in range(mid, start - 1, -1):
        if mylist[i] == key:
            left_count += 1
        else:
            break
    max_left_length = left_count
    res.left_size=max_left_length
    right_count = 0
    for i in range(mid + 1, end + 1):
        if mylist[i] == key:
            right_count += 1
        else:
            break
    max_right_length = right_count
    res.right_size = max_right_length

    maxVal= max(left_length, right_length, max_left_length + max_right_length)
    res.longest_size=maxVal
    return maxVal


def longest_run_recursive(mylist, key):
    res = Result(0,0,0,False)
    return longest_run_rec(mylist, key, 0, len(mylist) - 1,res)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


