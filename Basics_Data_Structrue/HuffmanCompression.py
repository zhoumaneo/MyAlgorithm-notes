# Huffman Compression
# 原理：用较少的bit表示出现频率较大的字符，用较多的bit表示出现频率较少的字符
# 参考：https://en.wikipedia.org/wiki/Huffman_coding
# HuffmanCompression code:
import collections
import heapq
def get_rate(compressed_binary, uncompressed_bits):
    return len(compressed_binary)*100 / uncompressed_bits

class HuffmanCompression:
    class Trie:
        def __init__(self,val,char=''):
            self.val = val
            self.char = char
            self.coding = ''
            self.left = self.right = None
        def __cmp__(self, other):
            return self.val - other.val
    def __init__(self,string):
        self.string = string
        counter = collections.Counter(string)
        heap=[]
        for char,cnt in counter.items():
            heapq.heappush(heap,HuffmanCompression.Trie(cnt, char))
        while len(heap)!=1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            trie = HuffmanCompression.Trie(left.val+right.val)
            trie.left,trie.right = left,right
            heapq.heappush(heap,trie)
        self.root = heap[0]
        self.s2b = {}
        self.bfs_encode(self.root,self.s2b)
    def bfs_encode(self,root,s2b):
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.char:
                s2b[node.char] = node.coding
                continue
            if node.left:
                node.left.coding = node.coding + '0'
                queue.append(node.left)
            if node.right:
                node.right.coding = node.coding + '1'
                queue.append(node.right)
    def compress(self):
        bits = ''
        for char in self.string:
            bits += self.s2b[char]
        return bits
    def uncompress(self,bits):
        string = ''
        root = self.root
        for bit in bits:
            if bit == '0':
                root = root.left
            else :
                root = root.right
            if root.char:
                string += root.char
                root = self.root
        return string
if __name__ == '__main__':
    s = 'everyday is awesome!'
    bits = len(s)*8
    hc = HuffmanCompression(s)
    compressed = hc.compress()
    print('compressed binary:' + compressed)
    print('uncompressed binary:' + hc.uncompress(compressed))
    print(hc.s2b)
    print('Huffman Compression-compress rate: %d%%' % get_rate(compressed, bits))
