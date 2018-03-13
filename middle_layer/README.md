Notes
====

### Tasks:

1. Identifying where the coding regions are and generating the coding DNA sequence

  - DONE. Checked against [online translation tool](https://web.expasy.org/translate/)

2. Aligning the protein translation with the DNA coding sequence

  - DONE

3. Identifying restriction enzyme (RE) sites

4. Providing a list of known REs to the front end

5. Identify whether an RE has restriction sites within the coding region

6. Counting codon usage in a gene

7. Calculating codon usage across all coding regions (perhaps use the subroutine developed for counting codon usage in a single gene) - store this somewhere; perhaps back in the database or in a text file.

8. Extracting information from the database layer (e.g. the complete gene list or individual gene information) (Some of these may simply be wrappers to database layer code)

  - [Output XML](http://stackabuse.com/reading-and-writing-xml-files-in-python/)

### General notes

**Receiving queries from the website CGI script:** Get the rest thing to talk to your python, look at the cgi script practical. Make a dummy cgi script or just get the call/link to work. Understand from this how your python files should be. should each function have a separate file/module? I should output XML. Query variables should have the same names as XML tags

**Getting acess to the database:** Call Adams python module.

