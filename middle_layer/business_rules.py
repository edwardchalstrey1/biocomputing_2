
""" Business logic"""

def get_coding_seq(origin_seq, cds_coordinates):

	""" Retrieves the coding sequence from a sequence string, given a list of sublists containing start and end coding positions
	
	>>> print(get_coding_seq("ggatccaatccagaatcccatactgcatttagttgtcatcttcttagtctctacaatct", [[1, 3], [17, 19], [25, 27]]))
	ggacccgca

	"""

	coding_seq = ""

	for start, end in cds_coordinates:

		coding_seq += origin_seq[start-1 : end]

	return coding_seq

def dna_codon_to_amino_acid(codon):

	""" Returns the single character representation of an amino acid as a string when given a string of the matching DNA codon

	>>> print(dna_codon_to_amino_acid('ttt'))
	F

	"""

	codon = codon.upper() # capitalization neccesary for return dictionary to work

	return {

		'TTT': 'F',
		'TTC': 'F',

		'TTA': 'L',
		'TTG': 'L',
		'CTT': 'L',
		'CTC': 'L',
		'CTA': 'L',
		'CTG': 'L',

		'ATT': 'I',
		'ATC': 'I',
		'ATA': 'I',

		'ATG': 'M',

		'GTT': 'V',
		'GTC': 'V',
		'GTA': 'V',
		'GTG': 'V',

		'TCT': 'S',
		'TCC': 'S',
		'TCA': 'S',
		'TCG': 'S',

		'CCT': 'P',
		'CCC': 'P',
		'CCA': 'P',
		'CCG': 'P',

		'ACT': 'T',
		'ACC': 'T',
		'ACA': 'T',
		'ACG': 'T',

		'GCT': 'A',
		'GCC': 'A',
		'GCA': 'A',
		'GCG': 'A',

		'TAT': 'Y',
		'TAC': 'Y',

		'TAA': 'Stop',
		'TAG': 'Stop',
		'TGA': 'Stop',

		'CAT': 'H',
		'CAC': 'H',

		'CAA': 'Q',
		'CAG': 'Q',

		'AAT': 'N',
		'AAC': 'N',

		'AAA': 'K',
		'AAG': 'K',

		'GAT': 'D',
		'GAC': 'D',

		'GAA': 'E',
		'GAG': 'E',

		'TGT': 'C',
		'TGC': 'C',

		'TGG': 'W',

		'CGT': 'R',
		'CGC': 'R',
		'CGA': 'R',
		'CGG': 'R',
		'AGA': 'R',
		'AGG': 'R',

		'AGT': 'S',
		'AGC': 'S',

		'GGT': 'G',
		'GGC': 'G',
		'GGA': 'G',
		'GGG': 'G'

	}.get(codon, 'X')



def check_alignment(dna_seq, amino_acid_Seq):

	""" When the coding dna sequence is taken from an entry from a Genbank file,
		the codons should already be aligned with the protein translation taken from that entry
	"""

	import re

	codons = re.findall('\w\w\w',dna_seq)



	return(codons)

#######################
### Test functions: ###
#######################

if __name__ == "__main__":

	import doctest

	doctest.testmod()