Notes
====

CHECK REST LECTURE

### Tasks:

1. Identifying where the coding regions are and generating the coding DNA sequence

   - DONE. Checked against [online translation tool](https://web.expasy.org/translate/)

2. Aligning the protein translation with the DNA coding sequence

   - Entries from the Genbank file appear to have the protein translation already ordered as per the coding sequence (determined by coordinates). My function checks if this is true
   - DONE

3. Identifying restriction enzyme (RE) sites

   - The ability to identify sticky-end [restriction enzyme sites](https://en.wikipedia.org/wiki/List_of_restriction_enzyme_cutting_sites:_E%E2%80%93F#Whole_list_navigation) in the genomic DNA - i.e. in both coding and non-coding regions. Restriction enzymes that cut in the 5' upstream and/or 3' downstream regions, but not in-between should be highlighted. At a minimum you should include the ability to search for EcoRI, BamHI and BsuMI - optionally you may include other enzymes.
   - DONE

4. Providing a list of known REs to the front end

   - Wrote a function that determines which of the 3 restriction enzymes we are most interested in ('EcoRI', 'BamHI', 'BsuMI'), are present in a sequence

5. Identify whether an RE has restriction sites within the coding region

   - See 4

6. Counting codon usage in a gene

   - DONE

7. Calculating codon usage across all coding regions (perhaps use the subroutine developed for counting codon usage in a single gene) - store this somewhere; perhaps back in the database or in a text file.

   - DONE

8. Extracting information from the database layer (e.g. the complete gene list or individual gene information) (Some of these may simply be wrappers to database layer code)

   - DONE

9. Check that all entries are aligned and if not, write a function to align

   - Create a dummy database (just in python) by using regex on the chromosome file, that just contains the coordinates, dna and translated protein

10. Write up what the output of ```get_entries()``` looks like for Trupti/Ilhan

### General notes

**Query functions I expect from database layer will be:**

- Ones that return a list:

  - all the gene names
  - proteins
  - genbank accession
  - chromosomal location

- Ones that return the DNA sequence with CDS coordinates and protein sequence based on a search for any of these:

  - gene identifiers (as given by a CDS /gene="XXXX" record in the Genbank file)
  - protein product names (as given by CDS /product="XXXX")
  - Genbank accession (as given by ACCESSION)
  - chromosomal location (e.g. 8q24.3, as given by source /map="XXXX")


### Follow up notes

Should get_entries() for a given gene id (or other search) only ever have one genbank entry in the result? i.e. the returned list only has one dictionary?
