#!/usr/bin/python3.4

import argparse

from Bio import Entrez, SeqIO
import time

parser = argparse.ArgumentParser(description="Downloads the nucleotide or protein sequences "
                                             " of the given genes.")

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
    database = "protein"

elif mol_type == "Genomic":
    term = term + " AND biomol_genomic[PROP]"
    database = "nucleotide"

elif mol_type == "Transcript":
    database = "nucleotide"
    term = term + " AND (biomol_mrna[PROP] OR biomol_rrna[PROP] OR biomol_crna[PROP]" \
                  " OR biomol_scrna[PROP] OR biomol_snrna[PROP] OR biomol_snorna[PROP] OR biomol_trna[PROP])"

search_handle = Entrez.esearch(db=database, term=term, retmax=20)
result = Entrez.read(search_handle)
search_handle.close()
#pprint(result)
print('For the %s query %s record(s) were found.' % (term, result['Count']))

for i in result['IdList']:
    print("\n", i)
    handle = Entrez.efetch(db='nuccore', id=i, rettype="gb", retmode="text")
    for seq_record in SeqIO.parse(handle, "gb"):
        print("%s %s..." % (seq_record.id, seq_record.description[:50]))
        print("Sequence length %i, %i features, from: %s"
              % (len(seq_record), len(seq_record.features), seq_record.annotations["source"]))
    handle.close()
    time.sleep(3)
    # print (record)

#     ID_output = Entrez.esummary(db='nucleotide', id=i)
#     out_dict = Entrez.read(ID_output)[0]
# pprint(out_dict)
#out = [out_dict['Accession'], out_dict['taxon'], out_dict['title']]
#print('\t'.join(out))
