"""
кодирование Хаффмана

По данной непустой строке s длины не более 10^4,
состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
"""

from collections import Counter, namedtuple
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


def main(string):
    text = string
    sorted_letters = Counter(text)
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
    translated = str_encode(code, text)
    answer = f'{len(code)} {len(translated)}'
    print(answer)
    for char, translation in code.items():
        print(f'{char}: {translation}')
    print(translated)
    return answer, code, translated


if __name__ == '__main__':
    assert main('a') == ('1 1', {'a': '0'}, '0')
    assert main('abacabad') == ('4 14', {'a':'0', 'b': '10', 'c': '110', 'd': '111'}, '01001100100111')
