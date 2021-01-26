# python3
import sys

def BWT(text):
    array = []
    array.append(text)
    for i in range(len(text) - 1):
        array.append(array[-1][-1]+array[-1][0:-1])
    array.sort()
    returnable = ""
    for i in range(len(text)):
        returnable += array[i][-1]
    return returnable

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))