#!/bin/bash
if [ $# -lt 6 ]; then
    echo "#csv-to-sc  Copyright (C) 2019  syed343 (GitHub)"
    echo "#This program comes with ABSOLUTELY NO WARRANTY; for details run with '--warranty'."
    echo "#This is free software, and you are welcome to redistribute it under certain conditions; run with '--copyright' for details."
    echo
fi
python3 csv_to_sc.py "$@"
