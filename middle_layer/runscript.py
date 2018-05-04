#!/usr/bin/env python3

#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

""" All code by Ed Chalstrey """

import for_database as fd
import pprint as pp
import business_rules as br
import dummy_data as dd

# pp.pprint(br.get_entries(prot="SMAD4"))

# pp.pprint(br.get_coding_seq('GAATTCAAAAAAAAAAAAGGATCCAAAAAAAAAAAACTCGAGAAAAAAAA', [[8, 16]]))

pp.pprint(dd.get_table_data_entire_chromosome())
