def even(value):
    return value % 2 == 0

def avg(list):
    total = 0
    for i in range(len(list)):
       total += list[i]
    avg = total / len(list)
    return avg

def max(list):
    max_value = list[0]    
    for i in range(len(list)):
       if max_value < list[i]:
          max_value = list[i]
    return max_value

def min(list):
    min_value = list[0]
    for i in range(len(list)):
       if min_value > list[i]:
          min_value = list[i]
    return min_value