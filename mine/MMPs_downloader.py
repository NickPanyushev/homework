#!/usr/bin/python3.4

from Bio import Entrez
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description="Downloads the nucleotide and protein sequences "
                                             " of the given genes")

parser.add_argument("gene",
                    type=str,
                    help="Gene name for searching the nucleotide database")

parser.add_argument("organism",
                    nargs='?',
                    type=str,
                    help="Organism to search sequences for")

parser.add_argument("mol_type",
                    nargs='?',
                    type=str,
                    choices=["Genomic", "Transcript", "Protein"],
                    help="Type of the biomolecule to find")

parser.add_argument("refseq",
                    nargs=1,
                    type=bool,
                    default=
                    choices = ["Genomic", "Transcript", "Protein"],
                              help = "Search only in RefSeq database")

args = parser.parse_args()
mol_type = args.mol_type
gene = args.gene
organism = args.organism

Entrez.email = 'panyushev@nextmail.ru'

term = gene + '[GENE]'

if organism:
    term = term + 'AND ' + organism + '[ORGN]'

if mol_type == "Genomic":
    term = term + ' AND ' + "biomol_genomic[PROP]"

elif mol_type == "Transcript":
    term = term + ' AND ' + "(biomol_mrna[PROP] OR biomol_rrna[PROP] OR biomol_crna[PROP]" \
                            " OR biomol_scrna[PROP] OR biomol_snrna[PROP] OR biomol_snorna[PROP] OR biomol_trna[PROP])"

    handle = Entrez.esearch(db='nucleotide', term=term)

elif mol_type == "Protein":
    term = term + ' AND ' + 
    handle = Entrez.esearch(db='protein', term=term)

result = Entrez.read(handle)
# print(result)

# for i in result['IdList']:
#     ID_output = Entrez.esummary(db='nucleotide', id=i)
#     out_dict = Entrez.read(ID_output)[0]
# print(out_dict)
# out = [out_dict['Accession'], out_dict['taxon'], out_dict['title']]
# print('\t'.join(out))
