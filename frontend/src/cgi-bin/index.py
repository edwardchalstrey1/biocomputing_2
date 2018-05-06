#!/usr/local/bin/python3
""" 
Programme:  Index
File:       index.py
Version:    V5
Date:       12/04/18
Function:   Get Gene information for Chromosome 18.

Copyright:  (c) Trupti Gore, Birkbeck College, 2018
Author:     Trupti Gore
Address:    Msc Bioinformatics with Systems Biology (First Year)
            Department of Biological sciences
            Birkbeck,University of London
            London WC1E 7HX

Description:
------------

This programme accepts a Gene id or Location or Accession Number or Protein name for the genes
on Chromosome 18. When the form is submitted then it calls another CGI script called query.py.

-----------------------------------------------------------------------------------------------------------


"""
#***********************************************
print("Content-Type: text/html\n")

# ******** Import libraries and Middle Layer's function files********
import cgi;
import cgitb
import business_rules as br

#******* Get the values from middle layer to display on the form****************
gene_list = br.get_gene_list()
acc_list=br.get_genbank_accession_list()
prot_list=br.get_protein_product_list()
loc_list=br.get_chromosomal_location_list()



#****************** Main CGI Script to display data ***************


html = "<html>\n"

html += "<head>\n"
html+="<?xml version='1.0' encoding='iso-8859-1'?>"
html+="<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.1//EN''http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd>"
html+="<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en'>"
html += "<title> Chromosome 18 </title>\n"
html+="<link rel='stylesheet' href='/frontend/src/html/css/bootstrap.min.css'></script>\n"
html+="<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>\n"
html+="<script src='/frontend/src/html/js/bootstrap.min.js'></script>\n"
html += "<link rel='stylesheet'  href='/frontend/src/html/css/style.css' type='text/css' />\n"
html+="<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
html += "</head>\n"

html += "<body onload=document.getElementById(\"submit\").disabled=true>\n"
html+="<div class='container'>\n"
html+="<div class='row'>\n"
html+="<section class='titlebox'>"
html+="<h1 class=center> Group 1 : Chromosome 18 </h1>\n"
html+="<p class='center'> This is a simple genome browser to look at the genes in Human chromosome 18 .The information displayed is based on the human genomic DNA records from  Genbank .</p>"
html+="<p class='center'>From the drop down lists please select either the Gene Name, Protein Product Name, Genbank Accession or Chromosomal Location to find out more information</p>\n"

html+="</section>"
html+="</div>"
html+="</div>"
html+="<form action='query.py' method='post' onreset=enable()>\n"

#****** Display gene information into following 4 dropdown lists for the user to select.

html+="<div class='container'>\n"
html+="<div class='row'>\n"
html+="<div class='col-sm-3' id='div-gene -info' class='dropdown'>\n"
html+="<h4> Gene Name </h4>\n"
html+="<select name='Gene' id='geneid' onClick=disable(id)>\n" 

   
for gene in gene_list:
   html+="<option id='opt-gene'>" +  gene + "</option>" 
	
html+="</select>\n"
html+="</div>\n"

html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Genbank Accession </h4>\n"
html+="<select name='Accession' id='accid' onClick=disable(id)>\n" 
   
for acc in acc_list:
   html+="<option id= 'opt-acc'>" +  acc + "</option>" 
	
html+="</select>\n"
html+="</div>\n"

html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Protein Product Name </h4>\n"
html+="<select name='Protein' id='protid' onClick=disable(id)>\n" 
   
for prot in prot_list:
   html+="<option id='opt-prot'>" +  prot + "</option>" 
	
html+="</select>\n"
html+="</div>\n"
html+="<div class='col-sm-3' id='div-gene-info' class='dropdown'>\n"
html+="<h4> Chromosomal Location </h4>\n"
html+="<select name='Location' id='locid' onClick=disable(id)>\n" 
   
for loc in loc_list:
   html+="<option id='opt-loc'>" +  loc + "</option>" 
	
html+="</select>\n"
html+="</div>\n"

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
html+="<footer class='footer'>"
html+="<p>Group : 1 Chromosome: 18 </p>"
html+="<script type='text/javascript' src='/frontend/src/html/js/lastmodified.js'></script>\n"
html+="<script type='text/javascript' src='/frontend/src/html/js/email.js'></script>\n"


html+=" </footer>"


html += "<script type='text/javascript' src='/frontend/src/html/js/biocw.js'></script>\n"

html += "</body>\n"

html += "</html>\n"

print(html)
