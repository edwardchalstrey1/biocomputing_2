
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



def are_sequences_aligned(dna_seq, amino_acid_seq):

	""" When the coding dna sequence is taken from an entry from a Genbank file,
		the codons should already be aligned with the protein translation taken from that entry

	>>> are_sequences_aligned('TTTTTAGCTTGTAAGAGT', 'FLACKS')
	True

	"""

	are_aligned = True

	import re

	codons = re.findall('\w\w\w', dna_seq)

	counter = 0

	for amino_acid in amino_acid_seq:

		if(amino_acid != dna_codon_to_amino_acid(codons[counter])):

			are_aligned = False

		counter += 1

	return(are_aligned)

def get_gene_list():

	genes = ['ABC', 'XYZ', 'ETC'] # dummy

	import xml.etree.ElementTree as ET

	genes_xml = ET.Element('genes')

	for gene in genes:

		gene_tag = ET.SubElement(genes_xml, 'gene')
		gene_tag.text = gene

	return(ET.tostring(genes_xml))

def count_codons(sequence):

	""" Splits the DNA sequence into triplet codons, starting from position 1 of the sequence
		and counts the frequency of codons, storing in a dictionary.

	>>> sequence = 'AAATTTCCCGGGAAA'

	>>> print(count_codons(sequence)['AAA'])
	2

	"""

	import re

	codons = re.findall('\w\w\w', sequence)

	codon_dict = {}

	for codon in codons:

		if codon not in codon_dict:

			codon_dict[codon] = 1

		else:

			codon_dict[codon] += 1

	return(codon_dict)

def find_restriction_sites(enzyme, sequence):

	""" Find the start/end positions of cutting sites for a given restriction enzyme in a DNA sequence,
		with the first position in the sequence as 1 (not 0)

	>>> sequence = 'XXXGAATTCXXXCTTAAG'

	>>> find_restriction_sites('EcoRI', sequence)
	[[4, 9], [13, 18]]

	"""

	sequence = sequence.upper()

	enzyme_5prime_dict = {

		'EcoRI': 'GAATTC',
		'BamHI': 'GGATCC',
		'BsuMI': 'CTCGAG'

	}

	enzyme_5prime_seq = enzyme_5prime_dict.get(enzyme, 'N/A')

	enzyme_3prime_seq = enzyme_5prime_seq[::-1] # 3 prime seq is reverse of 5 prime seq

	coordinates = []

	import re
	
	p = re.compile(enzyme_5prime_seq)

	for m in p.finditer(sequence):

		coordinates.append([m.start() + 1, m.start() + len(enzyme_5prime_seq)])

	p = re.compile(enzyme_3prime_seq)

	for m in p.finditer(sequence):

		coordinates.append([m.start() + 1, m.start() + len(enzyme_3prime_seq)])

	if len(coordinates) > 0:

		return(coordinates)

	else:

		return None

def which_enzymes_cut(sequence):
	
	""" Find out which of the restriction enzymes we are interested in have cutting sites in a sequence

	>>> sequence = 'GGATCCXXXGAATTC'

	>>> which_enzymes_cut(sequence)
	['EcoRI', 'BamHI']

	"""

	restriction_enzymes = ['EcoRI', 'BamHI', 'BsuMI']

	enzymes_for_this_sequence = []

	for enzyme in restriction_enzymes:

		if find_restriction_sites(enzyme, sequence) != None:

			enzymes_for_this_sequence.append(enzyme)

	return(enzymes_for_this_sequence)


#######################
### Test functions: ###
#######################

if __name__ == "__main__":

	import doctest

	doctest.testmod()