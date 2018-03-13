Notes
====

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

6. Counting codon usage in a gene

  - DONE

7. Calculating codon usage across all coding regions (perhaps use the subroutine developed for counting codon usage in a single gene) - store this somewhere; perhaps back in the database or in a text file.

8. Extracting information from the database layer (e.g. the complete gene list or individual gene information) (Some of these may simply be wrappers to database layer code)

  - [Output XML](http://stackabuse.com/reading-and-writing-xml-files-in-python/)

### General notes

**Receiving queries from the website CGI script:** Get the rest thing to talk to your python, look at the cgi script practical. Make a dummy cgi script or just get the call/link to work. Understand from this how your python files should be. should each function have a separate file/module? I should output XML. Query variables should have the same names as XML tags

**Getting acess to the database:** Call Adams python module.

