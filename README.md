NAME
    csv-to-sc - convert text files or user input after prompts into a .sc file

USAGE
    csv-to-sc [OPTIONS]

DESCRIPTION
csv-to-sc is a small program which converts a text file into a .sc file for use with the sc terminal spreadsheet editor.

USER OPTIONS (none of them is required):

    -f [input file (relative file path)]
        the text file from which to read (normally a .csv file)

    -d [string delimiter (with or without quotes)]
        the token by which each row will be split into cells

    -o [output (relative file path)]
        the file to which the sc code will be written

    -m [mode ('w' or 'a')]
        the mode to write in ('w' or 'a')

    -p
        print to standard output without prompting

Do not write options together (e.g. -fd).

If an option is not given, a prompt will ask for it (but see below about -p).
If all the options are given, then no user prompts are required. This is useful for Bash scripts.

If -p is given, then no prompt regarding writing to files will be given, except if -o has been specified while -m has not

There is one f-string in the codebase. F-strings don't work if the version of Python is less than 3.6
