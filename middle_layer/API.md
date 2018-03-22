What the middle layer requires from the back end
=============

Python functions contained in a wrapper module called e.g. "wrapper.py":

```get_gene_list()```

   - Returns the list of gene names stored in the database

```get_protein_product_list()```

   - Returns the list of protein products stored in the database

```get_genbank_accession_list()```

   - Returns the list of Genbank accessions stored in the database

```get_chromosomal_location_list()```

   - Returns the list of chromosomal locations stored in the database

```get_entries(gene=None, prot=None, acc=None, loc=None)``` (see my example in [dummy_data.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/dummy_data.py))

   - I should be able to provide a string of the gene, protein name, genbank accession or chromosomal location. You will then pull all the matching entries from the database (i.e. each entry in the Genbank file is an entry)
   - The function should returns a list of dictionaries. Each dict contains the gene, protein product, accession, location, CDS coordinates (ideally as a list of lists, see below), the full DNA seq and the translated amino acid seq
   - Follow the below dictionary structure:

   example_dict = {
		"gene": "VPS4B",
		"prot": "vacuolar protein sorting factor 4B",
		"acc": "AF282904",
		"cds": [[2676, 2702], [13357, 13468], [14489, 14645]],
		"dna": "ggatccaatccagaatcccat...",
		"aa": "MSSTSPNLQKAIDLASKAAQEDKAGN..."
	}

What the frontend should use from the middle layer
=========

Python functions contained in a module called [business_rules.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/business_rules.py). I have named them the same as functions I want from the database, so you can do:

```import business_rules as b```

```b.get_gene_list()```

   - Returns the list of gene names stored in the database

```b.get_protein_product_list()```

   - Returns the list of protein products stored in the database

```b.get_genbank_accession_list()```

   - Returns the list of Genbank accessions stored in the database

```b.get_chromosomal_location_list()```

   - Returns the list of chromosomal locations stored in the database

All of the above functions will be used to generate the lists genes, proteins etc to display on a page, each of which can be clicked. Clicking should send that gene name (or protein or chromosomal location etc) the following function, which will return all the information you need from the middle layer:

```b.get_entries(gene=None, prot=None, acc=None, loc=None)```

Provide a gene, protein, accession or chromosome location (i.e. the thing that is clicked on) to this function in the relevant parameter.

The function will return a list of dictionaries, with each dictionary corresponding to a relevant entry from the database. The dictionary will have the following structure:

example_dict = {
	"gene": "VPS4B",
	"prot": "vacuolar protein sorting factor 4B",
	"acc": "AF282904",
	"cds": [[2676, 2702], [13357, 13468], [14489, 14645]],
	"dna": "ggatccaatccagaatcccat...",
	"aa": "MSSTSPNLQKAIDLASKAAQEDKAGN...",
	"restriction_sites": {'BamHI': [[939, 944], [1000, 1005]]},
	"cds_seq": "atgtcatccacttcgcccaacctc...",
	'codon_count': {'aaa': 26, 'aac': 8, 'aag': 16, 'aat': 9}
}

- The dictionary under the key "restriction_sites" can have values for one or more of 'EcoRI', 'BamHI' and 'BsuMI' and the each sub-list in the list gives the start and end of a restriction site
- "codon_count" should have a value for every codon that appears in the coding sequence