# python3
import sys

def sort_characters(text):
    order = []
    chars = ["$","A","C","G", "T"]
    for char in chars:
        for i in range(len(text)):
            if char ==  text[i]:
                order.append(i)
    return order

def compute_char_classes(text , order):
    classes = [0]
    for i in range(1,len(text)):
        if text[order[i]] == text[order[i - 1]]:
            classes.append(classes[i- 1])
        else:
            classes.append(classes[i - 1] + 1)
    return classes

def sort_double_cyclic_Shifts(text, l, order, classes):
    new_order  = []
    count = []
    for i in range(len(text)):
        new_order.append(0)
        count.append(0)
    for i in range(len(text)):
        count[classes[i]] += 1
    for j in range(1,len(text)):
        count[j] += count[j-1]


    for i in range(len(text) -1 , -1, -1):
        start = (order[i] - l + len(text)) % len(text)
        print(start)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
        print(new_order)
    print()
    return new_order

def update_classes(order, classes, l):
    n = len(order)
    updated_classes = []
    for i in range(n):
        updated_classes.append(0)
    for i in range(1,n):
        cur =  order[i]
        prev = order[i-1]
        mid_cur = (cur + l) % n
        mid_prev = (prev + l) % n
        if classes[cur] == classes[prev]  and classes[mid_cur] == classes[mid_prev]:
            updated_classes.append(updated_classes[i-1])
        else:
            updated_classes.append(updated_classes[i - 1] +1)
    return updated_classes

def build_suffix_array(text):
    result = []
    order = sort_characters(text)
    classes = compute_char_classes(text,order)
    l = 1
    print(order)
    while l < len(text):
        order = sort_double_cyclic_Shifts(text,l, order, classes)
        classes = update_classes(order, classes, l)
        l *=2
    result = order
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))