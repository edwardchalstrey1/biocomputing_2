#############################################
### THIS SCRIPT USED FOR TESTING PURPOSES ###
#############################################

import business_rules as b
import pprint as pp

genes = b.get_gene_list()

pp.pprint(b.get_entries(gene="VPS4B")[0]["restriction_sites"]["BamHI"])

