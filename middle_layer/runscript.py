#!/usr/bin/env python3

#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

""" All code by Ed Chalstrey """

import for_database as fd
import pprint as pp
import business_rules as bp

# pp.pprint(fd.count_codons_all_coding_regions())
pp.pprint(bp.get_codon_usage_frequencies(['ATG', 'CCC', 'AAA']))

