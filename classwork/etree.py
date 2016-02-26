from lxml import etree
import requests


url = "http://larstheyeti.tumblr.com/"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter("img"):
    print(element.attrib["src"])

# tree = etree.parse("test.xml").getroot()
#
# sum = 0
# for score in tree.iter("score"):
#     sum += int(score.text)
# mean = sum / len(list(tree.iter("score")))
# print(mean)