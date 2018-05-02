Front End Documentation:

Imp Notes: 
The Shebang line might need to change from /usr/local/bin/python3 to /usr/bin/env python3 



The front end is developed to display the detailed information about the genes on the given chromosome -Chromosome 18 based on the user selection.

#### Requirements:  A server set-up, python 3

#### File structure:



	Server’s WWW folder --> index.html
			 
			 css-->stylesheets
						            
			 js-->JavaScript and jQuery files
			 
	CGI-Bin folder-->CGI scripts
						    
			 Python function files


#### Index.html: 
This page loads from the local server’s WWW folder. After loading it calls a function called `loadindex()` 
from the JavaScript file to load index.py

### Python function file used from the Middle Layer/Business Logic tier	
Business_rules.py

#### Index.py
   Following functions are used from business_rules.py
   
•	`get_gene_list()`

•	`get_genbank_accesion_list()`

•	`get_protein_prodcut_list()`

•	`get_chromosomal_location_list()`

These functions return respective lists which are used to populate 4 drop down lists.
After the user selects the values then the form is submitted with `post` method for query.py

#### query.py

Using the method `cgi.FieldStorage()` , the values from the form are stored into variables. 
Based on the input, the function `get_entries(gene=gene, prot=prot, acc=acc, loc=loc)` from business_rules is accessed. 
get_entries() returns a dictionary which has stored the information  for the respective entry. 

The gene dictionary gives 
-	Gene name

-	Protein product

-	Accession Number

-	Chromosomal Location

-	Coding region co-ordinates 

-	Amino acid for the coding region

-	Restriction enzyme cut sites for the enzymes (EcoRI,BamHI and BsuMI) and codon frequency dictionary 


#### Restriction enzyme site functionality
AngularJs `ng-switch` API directive is used where it chooses one of the nested elements and makes it visible based on the which element matches the value from evaluated expression.Here the user can select the restriction enzymes with the help of radio buttons and find if they cut within or outside the coding region. The restriction enzyme sites are highlighted only if they cut outside the coding region. This is checked by `check_res_enzyme()` function from functions.py file.


#### Functions.py 
This function file is written for the frontend to achieve following functionalities:

##### Highlight coding region
Following 2 functions are written.
`highlight_coding_seq()` : this function inserts the delimeters at the start and end of the coding region. An offset is used to check that the positions are not changed whilst inserting the delimiters

`hilite()` :  The delimeters are replaced by <mark class= ‘highlight’> which is predefined in the CSS file. Once it is done then the new highlighted DNA is displayed on the browser where the mark element is rendered accordingly.

Same principle is used to highlight the restriction enzyme cut sites.

`check_res_enzymes()` : This function checks if the restriction enzyme cut sites fall within the coding region or not.

#### BioCW.js:
This JavaScript file contains functions like enable() which resets the dropdown lists on the index.py , disable() which disables the other drop-down lists if one is selected, an event handler for accordion style display to display the codon frequency table.

#### jQuery.js:
This jQuery file has a document.ready event which scans the codon frequency and chromosome codon frequency table for the most overused and least overused codons and highlights the corresponding parent column with help of two more functions-findMaxVal() and findMinVal()

#### Lastmodified.js:
This jQuery function uses the HTML DOM's lastmodified property. 



