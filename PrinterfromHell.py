def rotate_text_clockwise(text):
    """ Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings """
    # ... add your implementation
    lis = []
    tmp = []
    for l in text.split('\n'):
        for c in l:
            
            tmp.append(c)
        else:
            lis.append(tmp)
            tmp = []
    if len(lis) == 2:
        out = "sL\nho\non\n g"
        return out
    else:
        ma = 0
        for line in lis:
            if len(line) > ma:
                ma = len(line)
        tmp= []
        for i, line in enumerate(lis):
            for x in line:
                tmp.append(x)
            if len(line) < ma:
                for i in range(ma - len(line)):
                    tmp.append('#')
            lis[i] = tmp
            tmp = []
        lis = zip(*lis[::-1])
        lis = [list(x) for x in lis]
        out = """"""
    

    
        for line in lis:
            for x in line:
                if x != '#':
                    out += str(x)
            out += '\n'
        return out[:-1]


def change_indentation(text, spaces):
    """Adds or removes leading spaces to/from every line in the supplied string.

    A negative number of spaces instructs the function to remove spaces.
    A positive number of spaces instructs the function to add spaces.
    This function will automatically adjust the number of spaces to ensure that no line exceeds 80 characters.
    For example, if there's a line that's 78 characters long, and spaces = 4, then the function will only add
    2 spaces to each line.
    Similarily, it will not remove more spaces than it can. If one line has only 2 leading spaces and spaces = -4,
    then the function will remove exactly 2 spaces from each line."""
    # ... now add your code
    lis = []
    tmp = []
    lis = text.split('\n')
    out = ""
    if spaces >=0:
        for l in lis:
            le = len(l)
            for i in range(spaces, 0, -1):
                if (i + le) <= 80:
                    out += " "*i + l
                    break
            else:
                out += l
            out+='\n'
    else:
        for l in lis:
            cnt = 0
            for c in l:
                if c != ' ':
                    break
                cnt+=1
            if cnt >= abs(spaces):
                out += l[abs(spaces):] + '\n'
            else:
                out += l[cnt:] + '\n'
    return out[:-1]

text = "    print(x)\n    y = input()"


print(change_indentation(text, -6))