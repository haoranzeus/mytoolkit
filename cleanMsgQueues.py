#!/usr/bin/python3
import os
import re

data = os.popen('ipcs -q').read()

lines = re.split('\n', data);

for line in lines:
    elements = re.split(' ', line)
    if len(elements) >= 2:
        if elements[1].isdigit():
            os.system('ipcrm -q' + elements[1])
