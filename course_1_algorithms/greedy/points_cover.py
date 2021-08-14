import io
from collections import deque

test1 = io.StringIO('''3
1 3
2 5
3 6''')

test2 = io.StringIO('''4
4 7
1 3
2 5
5 6''')

test3 = io.StringIO('''5
5 6
4 7
3 8
2 9
1 10''')

test4 = io.StringIO('''5
1 2
2 3
3 4
4 5
5 6''')

test5 = io.StringIO('''5
1 2
3 4
5 6
7 8
9 10''')


def main(str_buffer):
    sections_num = int(next(str_buffer))
    section_list = []
    for i in range(sections_num):
        left, right = (int(i) for i in next(str_buffer).split(' '))
        section_list.append((left, right))
    sorted_sections = deque(sorted(section_list, key=lambda x: x[1]))
    current_section = sorted_sections.popleft()[-1]
    output = [current_section]
    output_set = {current_section, }
    last_section = sorted_sections[-1][-1]
    while sorted_sections and current_section <= last_section:
        if sorted_sections[0][0] <= current_section <= sorted_sections[0][1]:
            sorted_sections.popleft()
            if current_section not in output_set:
                output_set.add(current_section)
                output.append(current_section)
        else:
            current_section = sorted_sections[0][1]
    len_output = len(output)
    second_result = ' '.join((str(i) for i in output))
    return len_output, output


if __name__ == "__main__":
    assert main(test1) == (1, [3])
    assert main(test2) == (2, [3, 6])
    assert main(test3) == (1, [6])
    assert main(test4) == (3, [2, 4, 6])
    assert main(test5) == (5, [2, 4, 6, 8, 10])
