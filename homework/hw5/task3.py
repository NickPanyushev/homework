import re
import sys

code = sys.stdin.read().split('\n')
result = [None for i in range(len(code)+1)]
regexp = "(\w+)\s+=\s+.*"
for index, string in enumerate(code, start = 1):
    result[index] = re.findall(regexp, string)
    if result[index]:
        print(index, result[index][0])
