Biocomputing 2 project for Birkbeck MSc
======

[Link to Andew Martin instructions](http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/index.html)

First task: Display gene identifiers list
----

**Adam:** Database with a table of all the gene ids. Python module with a function that contains the SQL query to get the list. e.g. ```get_gene_list()```

**Ed:** Python script that imports Adam's function and has a similarly named function. Exports the results to XML with tags like ```<gene>blah</gene>```

**Trupti/Ilhan:** HTML page with a button saying "Get list of genes in database" that displays the list. CGI script calls Ed's python function.