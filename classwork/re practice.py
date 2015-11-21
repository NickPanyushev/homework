import re
import requests
from urllib.parse import urlencode

def link_to_twitter(link): # функция, которая получает ссылку на твиттер
    response = requests.get(link)
    html_code = response.text
    regex = '<a href="http://twitter.com/[^\"]+" '
    results = re.findall(regex, html_code)
    return (results)

def find_smth():

    genes = input()
    query = {"term": genes}
    query_string = urlencode(query)
    url_gene = "http://www.ncbi.nlm.nih.gov/gene?" + query_string
    response = requests.get(url_gene)
    text = response.text
    results = re.findall("ID: \d+", text)
    return (results)

link = "http://bioinformaticsinstitute.ru/"
print (find_smth())
