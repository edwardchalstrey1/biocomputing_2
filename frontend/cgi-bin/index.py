#!/usr/bin/env python
""" 
Programme:  Index
File:       index.cgi

Version:    V5
Date:       12/04/18
Function:   Get Gene information for Chromosome 18.

Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX

----------------------------------------------------------------------------------------------------------

This programme is released under the GNU Public Licence (GPL V3)

----------------------------------------------------------------------------------------------------------

Description:
------------

This programme accepts a Gene id or Location or Accession Number or Protein name for the genes
on Chromosome 18.

-----------------------------------------------------------------------------------------------------------
Revision History:
-----------------
V5  12/04/18    Original    By: TG  Previous versions are not tracked.

"""
#***********************************************
print("Content-Type: text/html\n")

# ******** Import libraries and Middle Layer's function files********
import cgi;
import cgitb
import business_rules as br
import xml.etree.ElementTree as ET

#******* Get the values from middle layer to display on the form****************
gene_list = br.get_gene_list()
acc_list=br.get_genbank_accession_list()
prot_list=br.get_protein_product_list()
loc_list=br.get_chromosomal_location_list()

#******** Read the values from  xml string form
genes=ET.fromstring(gene_list)
accession=ET.fromstring(acc_list)
proteins=ET.fromstring(prot_list)
locations=ET.fromstring(loc_list)


#****************** Main CGI Script to display data ***************


html = "<html>\n"
html += "<head>\n"

html += "<title> Chromosome 18 </title>\n"
html+="<link rel='stylesheet' href='http://localhost/BioCW2/WWW/CSS/bootstrap.min.css'></script>\n"
html+="<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>\n"
html+="<script src='http://localhost/BioCW2/WWW/JS/bootstrap.min.js'></script>\n"

html += "<link rel='stylesheet'  href='http://localhost/BioCW/WWW/CSS/style.css' type='text/css' />\n"


html+="<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
html += "</head>\n"

html += "<body onload=document.getElementById(\"submit\").disabled=true>\n"
html+="<div class='container'>\n"
html+="<div class='row'>\n"
html+="<div class='titlebox'>"
html+="<h1 class=center> Group 1 : Chromosome 18 </h1>\n"
html+="</div>"
html+="</div>"
html+="</div>"
html+="<form action='query.py' method='post' onreset=enable()>\n"

#****** Display gene information into following 4 dropdown lists for the user to select.

html+="<div class='container'>\n"
html+="<div class='row'>\n"
html+="<div class='col-sm-3' id='div-gene -info' class='dropdown'>\n"
html+="<h4> Gene Name </h4>\n"
html+="<select name='Gene' id='geneid' onClick=disable(id)>\n" 

   
for gene in genes.iter(tag='gene'):
   html+="<option id='opt-gene'>" +  gene.text + "</option>" 
	
html+="</select>\n"
html+="</div>\n"

html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Accession </h4>\n"
html+="<select name='Accession' id='accid' onClick=disable(id)>\n" 
   
for acc in accession.iter(tag='accession'):
   html+="<option id= 'opt-acc'>" +  acc.text + "</option>" 
	
html+="</select>\n"
html+="</div>\n"

html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Protein id </h4>\n"
html+="<select name='Protein' id='protid' onClick=disable(id)>\n" 
   
for prot in proteins.iter(tag='protein'):
   html+="<option id='opt-prot'>" +  prot.text + "</option>" 
	
html+="</select>\n"
html+="</div>\n"
html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Location </h4>\n"
html+="<select name='Location' id='locid' onClick=disable(id)>\n" 
   
for loc in locations.iter(tag='location'):
   html+="<option id='opt-loc'>" +  loc.text + "</option>" 
	
html+="</select>\n"
html+="</div>\n"
#html+="<div class='col-md-2' id='div-gene -info'>\n"
#html+="<h4> Restriction Enzyme</h4>\n"
#html+="<select name='Location' id='locid' onClick=change(id)>\n" 
   
#html+="<select class='selectgene' name='Enzyme' id=enzid><option value='BamHI'>BamHI</option> <option value='BsuMI'>BsuMI</option><option value='EcoRI'>EcoRI</option> "
#html+="</select>\n"
#html+="</div>\n"
html+="</div>\n"
html+="</div>\n"
html+="<div class='container'>\n"
html+="<div class='row'>\n"
html+="<div class='select-buttons'>\n"
html+="<input type='submit' id='submit'>\n"
html+="</div>\n" 
html+="<div class='select-buttons'>"
html+="<input type='reset' id='reset'>\n"
html+="</div>\n"
html+="</div>\n"
html+="</div>\n"
html+="</form>"
html+="<div class='footer'> Trupti Gore"
html+="<script type='text/javascript' src='http://localhost/BioCW2/WWW/JS/lastmodified.js'></script>\n"
html+="</div>"
html += "<script type='text/javascript' src='http://localhost/BioCW2/WWW/JS/biocw2.js'></script>\n"

html += "</body>\n"

html += "</html>\n"

print(html)