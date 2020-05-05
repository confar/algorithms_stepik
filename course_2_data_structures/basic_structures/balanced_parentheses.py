"""
Проверить, верно ли расставлены скобки в коде. Если нет,
выдать индекс первой ошибки.

Вы разрабатываете текстовый редактор для
программистов и хотите реализовать проверку
корректности расстановки скобок. В коде могут
встречаться скобки []{}(). Из них скобки [,{
и ( считаются открывающими, а соответствующими им закрывающими скобками являются ],} и ).

В случае, если скобки расставлены неправильно, редактор должен
также сообщить пользователю первое место, где обнаружена ошибка.
В первую очередь необходимо найти закрывающую скобку, для которой либо нет соответствующей открывающей
(например, скобка ] в строке “]()”), либо же она закрывает не соответствующую ей открывающую скобку (пример: “()[}”).
Если таких ошибок нет, необходимо найти первую открывающую скобку,
для которой нет соответствующей закрывающей (пример: скобка ( в строке “{}([]”).
"""

from collections import namedtuple
from typing import List, Any

paren_map = {'{': '}',
             '(': ')',
             '[': ']'}


class EmptyStack(Exception):
    pass


StackValue = namedtuple('StackValue', ['value', 'index'])


class Stack:
    __slots__ = ['array']

    def __init__(self) -> None:
        self.array: List[StackValue] = []

    def pop(self) -> StackValue:
        if not self.is_empty():
            return self.array.pop()
        raise EmptyStack

    def top(self) -> StackValue:
        if not self.is_empty():
            return self.array[-1]
        raise EmptyStack

    def is_empty(self) -> bool:
        return not self.array

    def push(self, value: StackValue) -> None:
        self.array.append(value)


def balanced_paratheses(parens: str) -> Any:
    stack = Stack()
    for i, value in enumerate(parens, start=1):
        if value in paren_map.keys():
            stack.push(StackValue(value, i))
        elif value in paren_map.values():
            if not stack.is_empty():
                top = stack.pop()
                if paren_map[top.value] != value:
                    return i
            else:
                return i
    if stack.is_empty():
        return 'Success'
    last_non_matching_bracket_index = stack.pop().index
    return last_non_matching_bracket_index


def main():
    assert balanced_paratheses('{') == 1
    assert balanced_paratheses('{[]') == 1
    assert balanced_paratheses('{{{') == 3
    assert balanced_paratheses('[]([]') == 3
    assert balanced_paratheses('{{{[][][]') == 3
    assert balanced_paratheses('{{{{{{{((()))}') == 6
    assert balanced_paratheses('{()}{') == 5
    assert balanced_paratheses('}()') == 1
    assert balanced_paratheses('()}()') == 3
    assert balanced_paratheses('}()') == 1
    assert balanced_paratheses('{[()]}}()') == 7
    assert balanced_paratheses('dasdsadsadas]]]') == 13
    assert balanced_paratheses('{}()') == "Success"
    assert balanced_paratheses('({}[(((())))])') == "Success"
    assert balanced_paratheses('()') == "Success"
    assert balanced_paratheses('({})') == "Success"
    assert balanced_paratheses('foo(bar({ <some initialization> })[i])') == "Success"
    assert balanced_paratheses('([](){([])})') == "Success"
    assert balanced_paratheses('()[]}') == 5
    assert balanced_paratheses('{{[()]]') == 7
    assert balanced_paratheses('{{{[][][]') == 3
    assert balanced_paratheses('{*{{}') == 3
    assert balanced_paratheses('[[*') == 2
    assert balanced_paratheses('{{') == 2
    assert balanced_paratheses('{{{**[][][]') == 3


if __name__ == '__main__':
    main()
