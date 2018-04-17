Middle layer documentation
======

I have provided instructions on how to use the middle layer for the database and front end developers in [middle_layer/API.md](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/API.md). In this documentation, I'll summarise how all of the relevant subroutines work and describe how the API is used by the front end, as well as detailing how the information on chromosome codon usage is stored in the database.

The subroutines used by the front end are kept in [middle_layer/business_rules.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/business_rules.py) and can be accessed in Python by the front end by importing this file as a module. They are as follows:
----

### Functions that pull data straight from the database, for usage by the front end directly:

1. ```get_gene_list()``` - returns a list of all the gene names in database (i.e. one for each Genbank file entry/record, denoted by CDS /gene="XXXX")
2. ```get_protein_product_list()``` - returns a list of all the protein products in the database (denoted by CDS /product="XXXX" for each record)
3. ```get_genbank_accession_list()``` - returns a list of all the genbank accessions (ACCESSION)
4. ```get_chromosomal_location_list()``` - returns a list of all the chromosomal locations (source /map="XXXX")
5. ```get_table_data_entire_chromosome()``` - returns a dictionary with each key being a DNA triplet codon (string) and the values containing information to populate a codon usage table.

The first 4 of the functions listed above extract data from the database that the database developer has extracted from the Genbank file directly. The fifth, extracts data that has been pre-calculated by the middle layer and stored in the database, which I will go on to explain below.

###  Functions that perform calculations, not for use by the front end directly

1. ```get_coding_seq(origin_seq, cds_coordinates)``` - returns the coding sequence from a sequence string, given a list of sublists containing start and end coding positions
2. ```dna_codon_to_amino_acid(codon)``` - returns the single character representation of an amino acid as a string when given a string of the matching DNA codon
3. ```are_sequences_aligned(dna_seq, amino_acid_seq)``` - checks whether a dna sequence and amino acid sequence are aligned and returns True/False
4. ```generate_polypeptide(dna_seq)``` - returns an amino acid sequence translation of a DNA sequence
5. ```count_codons(sequence)``` - returns a dictionary of all the triplet codons found in the sequence (starting from position 1 reading frame) with their frequency/count as the values of the codon keys
6. ```find_restriction_sites(enzyme, sequence)``` - returns a list of sub-lists with start and end positions of the given enzyme's restriction site(s) on the sequence. Works for an input string of 'EcoRI', 'BamHI' or 'BsuMI' to ```enzyme``` and any DNA sequence
7. ```which_enzymes_cut(sequence)``` - returns a list of one or more of the enzyme strings 'EcoRI', 'BamHI' or 'BsuMI' that cut the sequence
8. ```get_table_data(codon_dict)``` - returns the data required to populate a codon usage table. Uses as input a pre-calculated dictionary of codon counts (generated with ```count_codons(sequence)```). The output returned is a dictionary of dictionaries, one for each possible codon of the genetic code. Each sub-dictionary contains the amino acid of the codon, the frequency the codon is used per 100 codons and the ratio of that codon relative to all other codons with the same amino acid

All these functions are tested using **doctest**. The tests are run by typing ```python business_rules.py``` in the command line (from within the middle_layer dir). An additional manual test is described in [middle_layer/tests.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/tests.py).

### Main function used directly by the front end, pulling together all the data from a Genbank record with information calculated by the functions above (the API)

```get_entries(gene=None, prot=None, acc=None, loc=None)```

This function takes as input a gene, protein, accession or chromosome location in the relevant parameter.

The function will return a list of dictionaries, with each dictionary corresponding to an entry/record from the database with the matching gene, protein, accession or chromosomal location. *There should however only be one record that matches for a given search, so the returned list should only contain one dictionary.* The dictionary will have the following structure:

```
{
	"gene": "VPS4B",
	"prot": "vacuolar protein sorting factor 4B",
	"acc": "AF282904",
	"cds": [[2676, 2702], [13357, 13468], [14489, 14645]],
	"dna": "ATCG...",
	"aa": "MSSTSPNLQKAIDLASKAAQEDKAGN...",
	"cds_seq": "ATCG...",
	"restriction_sites": {'BamHI': [[939, 944], [1000, 1005]]},
	"codon_count": {'AAA': 26, 'AAC': 8, 'AAG': 16, 'AAT': 9},
	"table_data": {'GGT': {'aa': 'G', 'freq': 2.02, 'ratio': 0.3}, ...}
}

```

To get this information, a search is performed of the database for entries/records with the corresponding gene name (or protein or accession or chromosomal location) by calling a database layer function of the same name. This gives the values for "gene", "prot", "acc", "cds", "dna" and "aa". The coding sequence saved to the key "cds_seq" is determined with the ```count_codons``` function described above. Similarly, the values for "restriction_sites", "codon_count" and "table_data" are calculated with ```find_restriction_sites```, ```count_codons``` and ```get_table_data``` respectively. The other calculation functions described above are also used within ```get_entries```.

The subroutine used by the database layer to populate the database with data to be used for a codon usage table for the entire chromosome can be found in [middle_layer/for_database.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/for_database.py) 
-----

This file can be imported as a module to a Python script and used within code being run to populate the database.

The single function is called ```store_table_data_entire_chromosome()```, which outputs a dictionary of dictionaries, one for each possible codon of the genetic code. Each sub-dictionary contains the amino acid of the codon, the frequency the codon is used per 100 codons and the ratio of that codon relative to all other codons with the same amino acid.

To calculate this, the DNA sequence associated with each record is retrieved from the database layer, then the ```count_codons``` and ```get_table_data``` functions imported from business_rules.py are utilised, resulting in the same output as ```get_table_data```, but for the entire chromosome, instead of a single Genbank record.

Once this data is stored in the database, it can be retrieved by the front end via the middle layer as described above with ```get_table_data_entire_chromosome```.