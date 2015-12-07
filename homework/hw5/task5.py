import re
import sys

code = sys.stdin.read()
regexp = re.compile('(\W)+')
print(regexp.sub(' ', code))