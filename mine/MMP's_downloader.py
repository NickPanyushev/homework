#!/usr/bin/python3.4

from Bio import Entrez
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description="GSE-loader finds the GSE dataset "
                                             " by the search query")

parser.add_argument("query",
                    type=str,
                    help="Query for searching the GSE database")

parser.add_argument("organism",
                    nargs='?',
                    type=str,
                    help="Organism to search GSE's for")

args = parser.parse_args()
query = args.query
organism = args.organism

Entrez.email = 'panyushev@nextmail.ru'

if organism:
    term = organism + '[Organism]' + 'AND ' + query + '[All Fields]'
else:
    term = query + '[All Fields]'

handle = Entrez.esearch(db='gds', term=term)
result = Entrez.read(handle)

for i in result['IdList']:
    ID_output = Entrez.esummary(db='gds', id=i)
    out_dict = Entrez.read(ID_output)[0]
    out = [out_dict['Accession'], out_dict['taxon'], out_dict['title']]
    print('\t'.join(out))
