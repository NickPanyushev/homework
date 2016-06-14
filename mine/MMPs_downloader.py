#!/usr/bin/python3.4

from Bio import Entrez
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description="Downloads the nucleotide and protein sequences "
                                             " of the given genes")

parser.add_argument("gene",
                    type=str,
                    help="Gene name for searching the database")

parser.add_argument("type",
                    nargs='?',
                    metavar='type',
                    default="Genomic",
                    type=str,
                    choices=["Genomic", "Transcript", "Protein"],
                    help="Type of the biomolecule to find:"
                         " Genomic, Transcript, Protein")

parser.add_argument("-refseq",
                    nargs='?',
                    type=str,
                    default="n",
                    choices=["y","n"],
                    help="Search only in RefSeq database")

parser.add_argument("-orgn",
                    nargs='?',
                    type=str,
                    help="Organism to search sequences for")

args = parser.parse_args()
gene = args.gene
mol_type = args.type
refseq = args.refseq
organism = args.orgn

Entrez.email = 'panyushev@nextmail.ru'

term = gene + '[GENE]'

if organism:
    term = term + ' AND ' + organism + '[ORGN]'


if refseq == "y":
    term = term + ' AND refseq[filter]'

if mol_type == "Protein":
    handle = Entrez.esearch(db='protein', term=term)

elif mol_type == "Genomic":
    term = term + " AND biomol_genomic[PROP]"
    handle = Entrez.esearch(db='nucleotide', term=term)

elif mol_type == "Transcript":
    term = term + " AND (biomol_mrna[PROP] OR biomol_rrna[PROP] OR biomol_crna[PROP]" \
                  " OR biomol_scrna[PROP] OR biomol_snrna[PROP] OR biomol_snorna[PROP] OR biomol_trna[PROP])"
    handle = Entrez.esearch(db='nucleotide', term=term)



result = Entrez.read(handle)
#pprint(result)

for i in result['IdList']:
    print(i)
#     ID_output = Entrez.esummary(db='nucleotide', id=i)
#     out_dict = Entrez.read(ID_output)[0]
# print(out_dict)
#out = [out_dict['Accession'], out_dict['taxon'], out_dict['title']]
#print('\t'.join(out))
