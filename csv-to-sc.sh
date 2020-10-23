#!/bin/bash

if [ $(python3 -c "print('$@'.count('--silent'))") -eq 0 ]; then
    if [ $(python3 -c "print('$@'.count('-s'))") -eq 0 ]; then
        echo "#csv-to-sc  Copyright (C) 2019  syed343 (GitHub)"
        echo "#This program comes with ABSOLUTELY NO WARRANTY; for details run with '--warranty'."
        echo "#This is free software, and you are welcome to redistribute it under certain conditions; run with '--copyright' for details."
        echo
    fi
fi
python3 main.py "$@"
