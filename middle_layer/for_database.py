#!/usr/bin/env python3

""" Middle layer: function(s) for use by the database layer """

import dummy_data as dd
import business_rules as br

def count_codons_all_coding_regions():

	""" Gets a dictionary with keys as codons and values as the aggregate counts of the codons for coding regions of all the sequences in the database"""

	codon_dict = {}

	for entry in dd.get_entries(all=True):

		coding_seq = br.get_coding_seq(entry["dna"], entry["cds"])

		entry_codon_dict = br.count_codons(coding_seq)

		for codon, count in entry_codon_dict.items():

			if codon not in codon_dict:

				codon_dict[codon] = count

			else:

				codon_dict[codon] += count

	return(codon_dict)