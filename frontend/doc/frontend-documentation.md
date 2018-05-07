## Front End Documentation:

#### Imp Notes: 
If the Shebang line /usr/local/bin/python3  does not work then change it to /usr/bin/env python3 or /usr/bin/env python depending on the python directory path on the local machine.



The front end is developed to display the detailed information about the genes on the given chromosome -Chromosome 18 based on the user selection.

## Requirements:  A server set-up and python 3

## File structure:



	Server’s WWW folder --> index.html
			 
			 css-->stylesheets
						            
			 js-->JavaScript and jQuery files
			 
	CGI-Bin folder-->CGI scripts
						    
			 Python function files




## Python function file used from the Middle Layer/Business Logic tier	
Business_rules.py

## Front Layer Files:

### Index.html: 
This page loads from the local server’s WWW folder. After loading it calls a function called `loadindex()` 
from the JavaScript `biocw.js` file to load index.py

### Index.py
   Following functions are used from business_rules.py
   
•	`get_gene_list()`

•	`get_genbank_accesion_list()`

•	`get_protein_prodcut_list()`

•	`get_chromosomal_location_list()`

These functions return respective lists which are used to populate 4 drop down lists.
After the user selects the values then the form is submitted (by clicking on **Submit** button) with `post` method for query.py

### query.py

Using the method `cgi.FieldStorage()` , the values from the form are stored into variables. 
These values are passed to the function `get_entries(gene=gene, prot=prot, acc=acc, loc=loc)` from business_rules which returns a gene dictionary with gene information for the respective entry. 

The gene dictionary gives 
-	Gene name

-	Protein product

-	Accession Number

-	Chromosomal Location

-	Coding region co-ordinates 

-	Amino acid for the coding region

-	Restriction enzyme cut sites for the enzymes (EcoRI,BamHI and BsuMI) and codon frequency dictionary 


#### Restriction enzyme site functionality
AngularJs `ng-switch` API directive is used where it chooses one of the nested elements and makes it visible based on the  element which matches the value from evaluated expression.Here the user can select the restriction enzymes with the help of radio buttons and find if they cut within or outside the coding region. The restriction enzyme sites are highlighted only if they cut outside the coding region. This is checked by `check_res_enzyme()` function from `functions.py` file.

For the ease of navigation **Home** button has been provided to navigate back to the index page.


## Functions.py 
This function file is written for the frontend to achieve following functionalities:

`highlight_coding_seq()` : this function inserts the delimeters at the start and end of the coding region. An offset is used to check that the positions are not changed whilst inserting the delimiters

`hilite()` :  The delimeters are replaced by <mark class= ‘highlight’> which is predefined in the CSS file. Once it is done then the new highlighted DNA is displayed on the browser where the mark element is rendered accordingly.

`highlight_res_site()`  and `hilite_res()` : To identify and highlight the restriction enzyme cut sites.

`check_res_enzymes()` : This function checks if the restriction enzyme cut sites fall within the coding region or not.

## style.css

This is an external css file which is written to style all html elements.

#### semantic markup
##### Document structure tags:

** header ** , ** footer ** , ** section ** , ** form ** ,
#### Textual meaning tags: 

** h1, h4 ** , ** em ** , ** mark **

## BioCW.js:
This JavaScript file contains following functions.

`enable()` : Enables the dropdown lists on the index.py on reset button click event or page refresh. 

`disable()` : Disables the other drop-down lists if one is selected. 

`loadindex()` : Loads index.py file on index.html's body onload() event.

`accordian style` : Creates an accordian which is used to display the codon usage tables.

## jQuery.js:

This jQuery file has a document.ready event which scans the codon frequency and chromosome codon frequency table for the overused and underused codons and highlights the corresponding parent column. Our project team came up with the following criteria to be used to calculate the following.

Overused codons : If the frequency of the said codon in Gene Codon Frequency table is more than 150% of the frequency of the same codon in the Chromosome Codon Frequency table then it is considered as an overused codon.

Underused Codons : If the frequency of the said codon in Gene Codon Frequency table is less than 50% of the frequency of the same codon in the Chromosome Codon Frequency table then it is considered as an underused codon.

Rare Codons : If the codon frequency in Chromosome Codon Frequency table is less than 0.50 then we would consider these codons as rare codons. However we decided to hightlight only those records where codon frequency of such codon in the Gene Codon Frequency Table is greater than it's frequency in the Choromosome Codon Frequency table as we thought that would be interesting information for the user.

## email.js

`printemail()` : Prints email in a format which is hidden from web scraping programmes.


## Lastmodified.js:
This jQuery function uses the HTML DOM's lastmodified property. 


#### Query String:
http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/gt002/query.py?Gene=SMAD4&Protein=SMAD4&Accession=AB043547&Location=18q21
