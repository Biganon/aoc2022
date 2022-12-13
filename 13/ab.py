with open("input", "r") as f:
    lines = f.read().splitlines()

def compare(left, right):
    if type(left) not in (int, list):
        left = eval(left)
    if type(right) not in (int, list):
        right = eval(right)
    if type(left) == int and type(right) == int: # two integers
        if left == right:
            return None
        elif left < right:
            return True
        else:
            return False
    elif type(left) == list and type(right) == list: # two lists
        idx = 0
        while True:
            try:
                result = compare(left[idx], right[idx])
            except IndexError:
                if len(left) < len(right):
                    return True
                elif len(left) > len(right):
                    return False
                else:
                    return None
            if type(result) == bool:
                return result
            else:
                idx += 1
                continue
    else: # one integer and one list (assuming input is sane)
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return compare(left, right)

def bubble(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if not compare(arr[j], arr[j+1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
# Part 1 :

packets = list(filter(lambda x:x, lines)) # keep only non-empty lines
sum_ = 0
idx = 0
while True:
    try:
        left, right = packets[idx*2:idx*2+2]
    except ValueError:
        break

    if compare(left, right):
        sum_ += (idx+1)
    idx += 1
print(sum_)

# Part 2 :

packets.append("[[2]]")
packets.append("[[6]]")
bubble(packets)
print((packets.index("[[2]]")+1) * (packets.index("[[6]]")+1))