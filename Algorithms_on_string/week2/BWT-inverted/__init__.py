# python3
#import time
import sys
def countSort(array, freqHashTable):
    array.append("$")
    busqueda = {}
    busqueda["A"] = 1
    for i in range(freqHashTable["A"]):
        array.append("A")
    busqueda["C"] = len(array)
    for i in range(freqHashTable["C"]):
        array.append("C")
    busqueda["G"] = len(array)
    for i in range(freqHashTable["G"]):
        array.append("G")
    busqueda["T"] = len(array)
    for i in range(freqHashTable["T"]):
        array.append("T")
    return busqueda

def InverseBWT(bwt):
    transform = []
    matrix = []
    inverted = []
    aparciones = {}
    aparciones["A"] = 0
    aparciones["G"] = 0
    aparciones["C"] = 0
    aparciones["T"] = 0
    aparciones["$"] = 0
    #print("freq table:",time.process_time())
    for char in bwt:
        aparciones[char] += 1
        transform.append([char, aparciones[char]])
    #print("transform, position:",time.process_time())
    busqueda = countSort(inverted, aparciones)
    #print("Sort:",time.process_time())
    matrix.append(inverted)
    matrix.append(transform)
    #print("Matrix append:",time.process_time())
    returnable = ""
    returnable +=matrix[0][0]
    i = 1
    char = matrix[1][0][0]
    aparicion  = 1
    while char != "$":
        i = busqueda[char] + aparicion - 1
        returnable += matrix[0][i]
        char = matrix[1][i][0]
        aparicion = matrix[1][i][1]
    # write your code here
    return returnable[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    ##print("Lecture:",time.process_time())
    print(InverseBWT(bwt))
    #print(time.process_time())