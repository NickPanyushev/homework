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
                    default="Genomic",
                    type=str,
                    choices=["Genomic", "Transcript", "Protein"],
                    help="Type of the biomolecule to find")

parser.add_argument("-refseq",
                    nargs='?',
                    type=bool,
                    default=False,
                    # choices=[True, False],
                    help="Search only in RefSeq database")

parser.add_argument("-orgn",
                    nargs='?',
                    type=str,
                    help="Organism to search sequences for")

args = parser.parse_args()
print(args)
gene = args.gene
mol_type = args.type
refseq = args.refseq
organism = args.orgn



Entrez.email = 'panyushev@nextmail.ru'

term = gene + '[GENE]'

if organism:
    term = term + ' AND ' + organism + '[ORGN]'
    print(term)

if refseq:
    term = term + ' AND refseq[filter]'
    print(term)

if mol_type == "Genomic":
    term = term + " AND biomol_genomic[PROP]"
    print(term)

elif mol_type == "Transcript":
    term = term + " AND (biomol_mrna[PROP] OR biomol_rrna[PROP] OR biomol_crna[PROP]" \
                  " OR biomol_scrna[PROP] OR biomol_snrna[PROP] OR biomol_snorna[PROP] OR biomol_trna[PROP])"
    print(term)

    # handle = Entrez.esearch(db='nucleotide', term=term)

elif mol_type == "Protein":
    print(term)

    #handle = Entrez.esearch(db='protein', term=term)


# result = Entrez.read(handle)


# print(result)

# for i in result['IdList']:
#     ID_output = Entrez.esummary(db='nucleotide', id=i)
#     out_dict = Entrez.read(ID_output)[0]
# print(out_dict)
# out = [out_dict['Accession'], out_dict['taxon'], out_dict['title']]
# print('\t'.join(out))
