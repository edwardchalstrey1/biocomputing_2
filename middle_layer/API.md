*This API document is for the use of the frontend/database developers*

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

```get_entries(gene=None, prot=None, acc=None, loc=None, all=False)``` (see my example in [dummy_data.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/dummy_data.py))

   - I should be able to provide a string of the gene, protein name, genbank accession or chromosomal location. You will then pull all the matching entries from the database (i.e. each entry in the Genbank file is an entry)
   - The function should returns a list of dictionaries. Each dict contains the gene, protein product, accession, CDS coordinates (ideally as a list of lists, see below), the full DNA seq, the translated amino acid seq and the location
   - Follow the below dictionary structure:

```

example_dict = {
	"gene": "VPS4B",
	"prot": "vacuolar protein sorting factor 4B",
	"acc": "AF282904",
	"cds": [[2676, 2702], [13357, 13468], [14489, 14645]],
	"dna": "ggatccaatccagaatcccat...",
	"aa": "MSSTSPNLQKAIDLASKAAQEDKAGN...",
	"loc": "18q21-q22"
}

```

If **all** is set to True, then this should pull all the entries from the database, which is required for the below:

What the back end should use from the middle layer
-----

I have made a function called ```store_table_data_entire_chromosome()``` in [for_database.py](https://github.com/edwardchalstrey1/biocomputing_2/blob/master/middle_layer/for_database.py) which outputs a dictionary of dictionaries, one for each possible codon of the genetic code. Each sub-dictionary contains the amino acid of the codon, the frequency the codon is used per 100 codons and the ratio of that codon relative to all other codons with the same amino acid.

To do this, the database layer function ```get_entries(all=True)``` is called.

For example the dictionary looks like this (that has a key for every possible triplet codon ):

```
{'GGT': {'aa': 'G', 'freq': 2.02, 'ratio': 0.3}, ...}
```

Final function for the middle layer to use from the backend
-----

Once the data from ```store_table_data_entire_chromosome()``` is stored in the database, the middle layer then needs to be able to retrieve this data.

The function ```get_table_data_entire_chromosome()``` should pull the data out in the same format as it went in.

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

```
example_dict = {
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

- The dictionary under the key "restriction_sites" can have values for one or more of 'EcoRI', 'BamHI' and 'BsuMI' and the each sub-list in the list gives the start and end of a restriction site
- "codon_count" should have a value for every codon that appears in the coding sequence
- "table_data" has a key for every possible triplet codon. Use this to make a table like [Andrew's example](http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/codon-usage.gif)
- DNA sequences are capitalised, unlike in the Genbank file

```b.get_table_data_entire_chromosome()```

   - This should return table data in the same format as the sub-dictionary above, but for all the sequences in the chromosome put together