# python3
import sys


def find_pattern(pattern, text):
  result = []
  string  = pattern + "$" + text
  prefix_array = Prefix(string)
  len_pattern  = len(pattern)
  for i in range(len(pattern), len(string)):
      if prefix_array[i] == len_pattern:
          result.append(i-2*len_pattern)
  return result

def Prefix(string):
    prefix_array = []
    border = 0
    for i in range(len(string)):
        prefix_array.append(0)
    for i in range(1,len(string)):
        while border > 0 and string[i] != string[border]:
            border = prefix_array[border - 1]
        if string[i] == string[border]:
            border += 1
        else:
            border = 0
        prefix_array[i] = border
    return prefix_array



if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))
