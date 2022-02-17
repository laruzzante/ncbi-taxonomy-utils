#!/usr/bin/env python3
import sys
from ete3 import NCBITaxa

ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()

# print('\nLINEAGE usage example: ./taxid.py Apis mellifera')
# print('LINEAGE output example: 7460, Apis mellifera, Hymenoptera\n')

taxnames = []
taxname = ' '.join(sys.argv[1:]).strip()
taxnames.append(taxname)

try:
    taxids = ncbi.get_name_translator(taxnames)
    taxid = str(taxids[taxname][0])
    lineage = ncbi.get_lineage(taxid)
except TypeError:
    print('Input TypeError. Input only takes a species name.\nUsage example: ./taxid.py Apis mellifera')


try:
    order = ''
    for el in lineage:
        rank_dict = ncbi.get_rank([el])
        rank = (rank_dict[el])
        if rank == 'order':
            order = el
            order = ncbi.get_taxid_translator([order])[el]
except TypeError:
    print('Input TypeError. Make sure to give correct input for NCBITaxa.get_rank() function')

print(f"{taxid}, {taxname}, {order}")
