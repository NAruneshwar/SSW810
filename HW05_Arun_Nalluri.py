"""This is the Home Work 5 code file"""


def reverse(s):
    """reverses the string """
    result = ''
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return(result)


def rev_enumerate(seq):   
    """this emulates the enumerate function in reverse"""
    counter = len(seq)-1
    for k in seq[::-1]:
        yield(counter, k)
        counter -= 1


def get_lines(file_path):
    """Used to get data from files and perform required operations"""
    try:
        fp = open(file_path, 'r')
    except FileNotFoundError:
        raise Exception(f"Can't open {file_path}", 'r')
    else:
        with fp:
            temp = ''
            for line in fp:
                if line.endswith('\\\n'):
                    temp = temp + line.strip('\\\n')
                    continue
                else:
                    line = temp+line
                    temp = ''
                if line.startswith('#'):
                    continue
                if '#' not in line:
                    yield(line.strip())
                else:
                    ind = line.index('#')
                    yield(line.strip()[:ind])


def find_second(target, sequence):
    """Used to return the second occurence of the target in the sequence"""

    if target not in sequence:
        return -1
    index = sequence.find(target)+1
    index2 = sequence.find(target, index)
    return index2
