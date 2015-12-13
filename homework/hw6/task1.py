import re

import requests
from lxml import etree


def wikilinks(url):
    page = requests.get(url).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(page, parser)
    links = []
    for element in tree.iter('a'):
        if element.attrib.get('href'):
            links.append(element.attrib.get('href'))
    regexp = re.compile('\/wiki\/.*')
    filtered_links = []
    for i in range(len(links)):
        if regexp.match(links[i]):
            filtered_links.append("https://en.wikipedia.org" + links[i])
    return filtered_links


def clicks(Url_start, Url_end, number_clicks):
    if number_clicks == 0:
        return None
    links = []
    print(links)
    links_start = wikilinks(Url_start)
    if Url_end in links_start:
        links = [Url_start, Url_end]
    else:
        for k in links_start:
            res = clicks(k, Url_end, number_clicks - 1)
            if res:
                links = [Url_start] + res
                break
    return '\n'.join(links)


print(clicks('https://en.wikipedia.org/wiki/Gone_Maggie_Gone', 'https://en.wikipedia.org/wiki/Theia_(planet)', 3))
