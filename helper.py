# Return array of string, each array member reprensents a line in file
def get_content(file_name, remove_eol=True):
    content = []
    f = open(file_name, 'r')
    while 1:
        line = f.readline()

        if line:
            if remove_eol:
                line = line.rstrip()
            content.append(line)
        else:
            break

    return content
