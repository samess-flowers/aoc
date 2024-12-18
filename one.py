#!env python3

def get_text_from_file(file) -> str:
    text = ''
    with open(file, mode = 'r', encoding='utf-8') as f:
        for line in f:
            text = text + line

    return text

def split_lines(text:str) -> "Generator[int]":
    split = text.split('\n')
    for line in split:
        if line == '':
            continue
        l, r = line.split()
        yield int(l), int(r)

def main() -> None:
    text = get_text_from_file('one.txt')
    splitter = split_lines(text)
    total = 0
    for l , r in splitter:
        total += abs(l - r)

    print(total)

if __name__ == '__main__':
    main()
