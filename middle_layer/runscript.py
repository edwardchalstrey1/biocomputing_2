#!/usr/bin/env python3

#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

""" All code by Ed Chalstrey """

import business_rules as b
import pprint as pp

genes = b.get_gene_list()

pp.pprint(b.get_entries(gene="VPS4B")[0]["restriction_sites"])

