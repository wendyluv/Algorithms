# python3
import sys



class Trie:
    def __init__(self, patterns):
        self.root = Node(None,None)
        self.generate_tree(patterns)
        pass
    def generate_tree(self, patterns):
        for pattern in patterns:
            self.node = self.root
            for char in pattern +"$":
                if self.node.next.get(char, True):
                    self.node.next[char] = Node(self.node, char)
                self.node = self.node.next[char]
    def show_content(self):
        self.node = self.root
        self.root.show_content()

class Node():
    def __init__(self, parent, char):
        self.next = {}
        self.parent = parent
        self.char = char
    def show_content(self):
        print(self.next.keys())
        for key in self.next.keys():
            self.next[key].show_content()



def solve (text, n, patterns):
    trie = Trie(patterns=patterns)
    answer = []
    ##trie.show_content()
    for i in range(len(text)):
        if search(text, trie, i):
            answer.append(i)
    return answer

def search(text, trie, i):
    current_nodes = trie.root.next
    future_nodes = {}
    while i < len(text) and current_nodes != {}:
        #print(current_nodes)
        current_char = text[i]
        for node in current_nodes.values():
            if node.char == current_char:
                for next_node in node.next.values():
                    future_nodes[next_node.char] = next_node
                    if next_node.char == "$":
                        return True
        current_nodes = future_nodes
        future_nodes = {}
        i += 1
    return False






text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')