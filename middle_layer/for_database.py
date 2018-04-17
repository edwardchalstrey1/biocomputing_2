#!/usr/bin/env python3

""" Middle layer: function(s) for use by the database layer. All code by Ed Chalstrey """

import dummy_data as dd # for use until the database layer functions become available
import business_rules as br

def store_table_data_entire_chromosome():

	""" Gets the data required for the codon table of the entire chromosome, for storage in the database.
		The output is a dictionary of dictionaries, one for each possible codon of the genetic code. Each sub-dictionary contains the amino acid
		of the codon, the frequency the codon is used per 100 codons and the ratio of that codon relative
		to all other codons with the same amino acid."""

	codon_dict = {}

	for entry in dd.get_entries(all=True):

		entry_codon_dict = br.count_codons(entry["dna"].upper())

		for codon, count in entry_codon_dict.items():

			if codon not in codon_dict:

				codon_dict[codon] = count

			else:

				codon_dict[codon] += count

	table_data = br.get_table_data(codon_dict)

	return(table_data)