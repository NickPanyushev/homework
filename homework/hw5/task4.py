import re
import sys

code = sys.stdin.read().split('\n')
result = {i: None for i in range(1, len(code) + 1)}
regexp = re.compile(' *([\w,. ]+) =\s+')
comment = re.compile('^\s*#')
for index, string in enumerate(code, start=1):
    if not comment.match(string):
        for i in regexp.findall(string):
            result[index] = i.split(', ')
    if result[index]:
        print(index, ' '.join(result[index]))
