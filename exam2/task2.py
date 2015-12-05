import re
import requests

with open('links.txt', encoding='UTF8') as file:
    res_file = open('email_addresses.txt', 'w+')
    for line in file:
        r = requests.get(line).text
        regexp = '[\w\.]+@[\w\.]+'
        result = re.findall(regexp, r)
        for i in res_file:
            if not re.findall(result, i):
                res_file.write('\n'.join(result))
