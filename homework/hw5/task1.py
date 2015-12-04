import re
import sys
data = sys.stdin.read()
results = re.findall("[Yy]ou", data)

print(len(results))