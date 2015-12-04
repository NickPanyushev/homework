import re
import sys

rx = '0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}'
for line in sys.stdin.read().split('\n'):
    result = re.findall(rx, line)
    if result:
        print(line)
