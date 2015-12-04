def generator_range(n):
    for i in range(n):
        yield i
x= generator_range(10)
#print(type(generator_range))
#print(type(x))
#print(next(x))

from lxml import etree

tree = etree.parse('/home/nickolay/python-course/classwork/test.xml').getroot()

sum=0
for score in tree.iter('score'):
    sum += int(score.text)
mean = sum / len(list(tree.iter('score')))
#print (mean)

import requests
url = "http://larstheyeti.tumblr.com/"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter('img'):
    print(element.attrib["src"])



