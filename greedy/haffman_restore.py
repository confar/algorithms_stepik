import sys


def main(str_buffer):
    char_num,  str_size = map(int, next(str_buffer).split(' '))
    translation_map = {}
    for _ in range(char_num):
        char, translation = next(str_buffer).strip().split(': ')
        translation_map[translation] = char
    str_to_decode = next(str_buffer)
    output = []
    index = 0
    end = 1
    while end <= len(str_to_decode):
        chars = str_to_decode[index: end]
        if chars in translation_map:
            output.append(translation_map[chars])
            index = end
        end += 1
    out = ''.join(output)
    print(out)


if __name__ == '__main__':
    main(sys.stdin)
