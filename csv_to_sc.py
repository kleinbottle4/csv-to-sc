#'csv_to_sc.py' is the main program for the csv-to-sc program.
#It  converts .csv files into .sc files.

GPL_COPYRIGHT = '''
#Copyright (C) 2019  syed343 (GitHub)

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.'''

GPL_WARRANTY = '''
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.'''

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see https://www.gnu.org/licenses/
#or https://github.com/syed343/csv-to-sc/blob/master/LICENSE/.'''

from parse_strings import is_subset, is_int, is_float, table_to_nums, num_to_sc_col
from table import Table

def main(args):

    show_gpl(args)

    delim = get_delimiter(args)

    table = Table(get_raw(args, delim))

    table.table = table_to_nums(table.table)

    sc_list = generate_sc_list(table)

    filename = get_filename(args)

    mode = get_write_mode(args, filename)

    output_list(sc_list, filename, mode)

    return 0

def show_gpl(args):
    if args.count('--copyright') >= 1:
        print(GPL_COPYRIGHT)
    if args.count('--warranty') >= 1:
        print(GPL_WARRANTY)

def next_arg(args, opt):
    return args[args.index(opt) + 1]

def get_delimiter(args):
    if args.count('-d') == 0:
        delim = input('#Delimiter: ')
    else:
        delim = next_arg(args, '-d')
    return delim

def get_raw(args, delim):
    if args.count('-f') == 0:
        #-f not given
        raw = []
        empty_input = False
        print('#Press enter on an empty line when done.')
        while empty_input == False:
            temp = input()
            if temp == '':
                empty_input = True
            else:
                raw.append(temp)
    else:
        #-f given
        file = open(next_arg(args, '-f'))
        text = file.read()
        file.close()
        #remove extra newline at the end
        if text[-1] == '\n':
            text = text[:-1]
        raw = text.split('\n')
    #return a 2d array
    return [i.split(delim) for i in raw]

def generate_sc_list(table):
    sc_list = []
    col_i = []
    for i in range(table.get_width()):
        col_i.append(num_to_sc_col(i))

    for i, row in enumerate(table.table):
        for j, elem in enumerate(row):
            d_type = type(elem)
            if d_type == int or d_type == float:
                prefix = 'let'
            else:
                prefix = 'leftstring'
                elem = '"{}"'.format(elem)
            sc_list.append('{0} {1}{2} = {3}'.format(prefix, col_i[j], i, elem))
    return sc_list

def get_filename(args):
    if args.count('-o') == 0:
        #-o not given
        if args.count('-p') == 0:
            #-p not given
            if input('#Write output to file? (Y/n) ').lower().startswith('y'):
                filename = input('#Filename: (c = cancel) ')
            else:
                filename = 'c'
        else:
            #-p given
            filename = 'c'
    else:
        #-o given
        filename = next_arg(args, '-o')
    return filename

def get_write_mode(args, filename):
    #filename 'c' means cancel
    if filename != 'c':
        if args.count('-m') == 0:
            mode = input('#write (w) append (a) cancel (c) ').lower()
        else:
            mode = next_arg(args, '-m')
        #make sure mode is valid (defaults to 'c')
        if mode.startswith('w'):
            mode = 'w'
        elif mode.startswith('a'):
            mode = 'a'
        else:
            mode = 'c'
    else:
        #if filename is 'c'ancel
        mode = 'c'
    return mode

def output_list(sc_list, filename, mode):
    if mode == 'c':
            print('\n'.join(sc_list))
    else:
        file = open(filename, mode)
        file.write('\n' + '\n'.join(sc_list) + '\n')
        file.close()

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
