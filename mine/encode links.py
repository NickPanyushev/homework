import re
import requests
from lxml import etree


def wikilinks(url):
    page = requests.get(url).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(page, parser)
    links = []
    for element in tree.iter('span'):
        #if element.attrib.get('href'):
        links.append(element.attrib.get('href'))
    regexp = re.compile('/wiki/')
    filtered_links = []
    for i in range(len(links)):
        if regexp.match(links[i]):
            filtered_links.append("https://en.wikipedia.org" + links[i])
    return filtered_links
with open('input.txt', 'a', encoding = 'UTF8'):



