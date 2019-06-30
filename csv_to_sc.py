from parse_strings import is_subset, is_int, is_float, table_to_nums, num_to_sc_col
from table import Table

def next(args, opt):
    return args[args.index(opt) + 1]

def main(args):
    if args.count('-d') == 0:
        delim = input('Delimiter: ')
    else:
        delim = next(args, '-d')

    if args.count('-f') == 0:
        table = Table(get_raw(delim))
    else:
        file = open(next(args, '-f'))
        text = file.read()
        if text[-1] == '\n':
            text = text[:-1]
        lines = text.split('\n')
        table = Table([i.split(delim) for i in lines])

    table.table = table_to_nums(table.table)
    sc_list = []
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    col_i = []
    for i in range(table.count_cols()):
        col_i.append(num_to_sc_col(i))
    for i, row in enumerate(table.table):
        for j, elem in enumerate(row):
            d_type = type(elem)
            if d_type == int or d_type == float:
                prefix = 'let'
            else:
                prefix = 'leftstring'
                elem = '"' + elem + '"'
            #f-strings don't work if version is before python3.6
            sc_list.append(f'{prefix} {col_i[j]}{i} = {elem}')

    if args.count('-o') == 0:
        if args.count('-p') == 0:
            if input('Write output to file? (Y/n) ').lower().startswith('y'):
                filename = input('Filename: (c = cancel) ')
            else:
                filename = 'c'
        else:
            filename = 'c'
    else:
        filename = next(args, '-o')

    if filename != 'c':
        if args.count('-m') == 0:
            mode = input('write (w) append (a) cancel (c) ').lower()
        else:
            mode = next(args, '-m')

        if mode.startswith('w'):
            mode = 'w'
        elif mode.startswith('a'):
            mode = 'a'
        else:
            mode = 'c'

    else:
        mode = 'c'

    if mode == 'c':
        print('\n'.join(sc_list))
    else:
        file = open(filename, mode)
        file.write('\n' + '\n'.join(sc_list) + '\n')
        file.close()

    return 0

def get_raw(delim):
    raw = []
    empty_input = False
    while empty_input == False:
        temp = input()
        if temp == '':
            empty_input = True
        else:
            raw.append(temp)
    return [i.split(delim) for i in raw]

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
