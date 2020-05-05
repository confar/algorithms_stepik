from collections import Counter, namedtuple
import sys
import heapq


class Leaf(namedtuple('Leaf', ['count', 'char'])):

    def walk(self, code, acc):
        code[self.char] = acc


class Node(namedtuple('Node', ['count', 'left', 'right'])):
    def walk(self, code, acc):
        if self.left:
            self.left.walk(code, acc + '0')
        if self.right:
            self.right.walk(code, acc + '1')


def str_encode(code, str1):
    for char, translation in code.items():
        str1 = str1.replace(char, translation)
    return str1


def main():
    str1 = sys.stdin.readline().strip()
    sorted_letters = Counter(str1)
    heap = []
    for count, (char, freq) in enumerate(sorted_letters.items()):
        heap.append((freq, Leaf(count, char)))
    heapq.heapify(heap)
    count = len(heap)
    while len(heap) > 1:
        freq1, left = heapq.heappop(heap)
        freq2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, Node(count, left, right)))
        count += 1
    [(_, root)] = heap
    code = {}
    acc = '0' if len(sorted_letters) == 1 else ''
    root.walk(code, acc)
    translated = str_encode(code, str1)
    print(f'{len(code)} {len(translated)}')
    for char, translation in code.items():
        print(f'{char}: {translation}')
    print(translated)


if __name__ == '__main__':
    main()
