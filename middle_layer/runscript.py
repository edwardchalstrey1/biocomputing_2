#!/usr/bin/env python3

#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

""" All code by Ed Chalstrey """

import for_database as fd
import pprint as pp
import business_rules as br

# pp.pprint(fd.count_codons_all_coding_regions())
# pp.pprint(br.get_codon_usage_frequencies(['ATG', 'CCC', 'AAA']))

seq = "ggatccaatccagaatcccatactgcatttagttgtca".upper()

codon_dict = br.count_codons(seq)

pp.pprint(br.get_table_data(codon_dict))

