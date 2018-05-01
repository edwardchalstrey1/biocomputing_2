#!/usr/bin/env python3


""" 
Programme:  Query CGI script
File:       query.py

Version:    V7...
            V7.1        Changed gene dict part
            V7.2        Added pre tag and changed label
            
Date:       12/04/18
Function:   Get Gene information for Chromosome 18 from index.cgi, process and display

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
on Chromosome 18 from index.cgi. After accepting the values it accesses the middle layer functions which inturn 
queries the database and passes the information back to this programme to display on the webpage.

-----------------------------------------------------------------------------------------------------------
Revision History:
-----------------
V7      12/04/18        Original    By: TG  Previous versions are not tracked.
V8      13/04/18        Added Codon Table
V8.1    16/04/18        Codon list from function

"""


print("Content-Type: text/html\n")	

#**************************************
#******Import python modules***********
#**************************************

import cgi;
import cgitb
cgitb.enable()
import re
import operator
from operator import itemgetter
import business_rules as br
import functions as f


#**************************************
#***Get form values from index.cgi*****
#**************************************


form=cgi.FieldStorage()
gid=form.getvalue("Gene")
acc=form.getvalue("Accession")
prot=form.getvalue("Protein")
loc=form.getvalue("Location")
res_enzyme=form.getvalue("Enzyme")

#*******************************************
#***** Access Gene information dictionary***
#*******************************************
#gene_dict=br.get_entries(gid,prot,acc,loc)  # Detailed information of the gene in a dictionary format
#print(br.get_entries("VPS4B"))  
gene_dict_list = br.get_entries(gid,prot,acc,loc)  

gene_dict = gene_dict_list[0] # Detailed information of the gene in a dictionary format, only use the first entry found, we are assuming no duplicates in database

protein=gene_dict['prot']
dna=gene_dict['dna'] # (Ed's comment - I think this should already be upper case)
gene_name=gene_dict['gene']
amino_acid=gene_dict['aa']
cds=gene_dict['cds']
res_site=gene_dict['restriction_sites']
gene_codon_dict=gene_dict['table_data']  
    

#******************************************************************
#*** Codon frequency table for the gene and entire chromosome******
#******************************************************************

chrom_codon_dict=br.get_table_data_entire_chromosome()

#******* Get Coding Sequence*********


coding_sequence=br.get_coding_seq(dna,cds)

#***********Get Amino Acid  - Aligned**********
aligned_amino_acid=''
for a in amino_acid:
    aligned_amino_acid += a + "  "
aligned_amino_acid+='stop'
#***************Highlight coding parts of the dna**************
original_dna=dna
dna=f.highlight_coding_seq(dna,cds)    
coding_highlighted_dna=f.hilight(dna)

 
#********** Restriction enzyme site. Highlight only*********** 
#*****if these sites are not found in between the start********
#*********and End of coding region.****************************

enzdict={} # Dictionary is pre populated to display the highlighted restriction enzymes according to the selection
for enzyme,coordinates in res_site.items():
    
    resflag=f.check_res_enzyme(enzyme,cds,res_site) # resflag checks if the restriction cut sites are outside the coding region.
    
    if resflag!='True':
        coordinates=sorted(coordinates, key=itemgetter(1))
        restricted_dna=f.highlight_coding_seq(original_dna,coordinates)
        restricted_dna=f.hilight_res(restricted_dna)
            
    else:
        
        restricted_dna=' The selected restriction enzyme {} cuts within the coding region and hence not a useful enzyme to use for the genetic manipulation of this gene.'.format(enzyme)     
    enzdict[enzyme]=restricted_dna    
   

i=0 # variable for indicator scale

#***********************************************
#************Main CGI Script********************
#***********************************************
	
html="<html>\n"
html+="<head>\n"
html+="<?xml version='1.0' encoding='iso-8859-1'?>"
html+="<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.1//EN''http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd>"
html+="<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en'>"
html+="<title> Detailed information about the Gene </title>\n"
html+="<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"


html+="<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>\n"
html+="<script src='/frontend/src/html/js/bootstrap.min.js'></script>\n"
html+="<link rel='stylesheet' href='/frontend/src/html/css/bootstrap.min.css'></script>\n"
html+="<script src='https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js'></script>"

html+="<link rel='stylesheet'  type='text/css'  href='/frontend/src/html/css/style.css'/>\n"
html+="</head>\n"
html+="<body ng-app=''>\n"  # Angular JS functionality to display restriction enzyme cut sites as per the user input
html+="<table name='GeneIntro'>"
html+="<tr>"
html+="<th class='firstcol'>"
html+="<p> Name  </p>"
html+="</th>"
html+="<td>"
html+="<pre>"
html+=gene_name
html+="</pre>"
html+="</td>"
html+="</tr>"
html+="</tr>"
html+="<tr>"
html+="<th>"
html+="<p> The protein </p>"
html+="</th>"
html+="<td>"
html+="<pre>"
html+=protein
html+="</pre>"
html+="</td>"
html+="</tr>"
html+="<tr>"
html+="<th>"
html+="<p> Coding Region Co-ordinates : </p>"
html+="</th>"
html+="<td>"

coding_coordinates=''
for c in cds:
   coding_coordinates+=''.join('%s'%c)
html+="<div class='scroll'>"
html+="<pre>"
html+=coding_coordinates
html+="</pre>"
html+="</div>"
html+="</td>"
html+="</tr>"
html+="</table>"

html+="<table name='GeneDetailInfo'>" # Table to display dna sequences
html+="<tr>"
html+="<td class='firstcol'>"
html+="<br>"
html+="<br>"
html+="<p>Approximate Indicator Scale for Coding Region</p>\n"
html+="<br>"
html+="<br>"
html+="<br>"

html+="<p> Highlighted coding region: </p>\n"
html+="<br>"
html+="<br>"
html+="<br>"
html+="<br>"
html+="<p> " 'Select Restriction Enzyme to check' "</p>\n"

html+="<form>"
html+="<input type='radio' ng-model='myVar' value='bm'>BamHI"
html+="<input type='radio' ng-model='myVar' value='bs'>BsuMI"
html+="<input type='radio' ng-model='myVar' value='ec'>EcoRI"  
html+="</form>"
html+="<br>"
html+="<br>"
html+="<br>"
html+="<br>"
html+="</td>"
html+="<td> " # second column
html+="<div class='scroll'>" # div to scroll
html+="<div class='child'>" # child for label

while i<len(dna):
    html+="<label>" +str(i)+"</label>"
    i+=250

html+="</div>"  # end label child


html+="<div class='child'>\n"  #first child
html+="<pre>\n"
html+=coding_highlighted_dna 
html+="</pre>\n"
html+="</div>\n"            # end first child


html+="<div id= 'res_dna' class='child'>\n" # thild child
#html+="<div id='showHide' display = none'>\n"
html+="<div ng-switch='myVar'>"  # parent div of angular.    AngularJS code reference: https://www.w3schools.com/angular/tryit.asp?filename=try_ng_form_radio
html+="<div ng-switch-when='bm'>" # first child div of angular
html+="<pre>" + enzdict['BamHI'] +"</pre>" 

html+="<pre>"+ str(res_site['BamHI']) + "</pre>" 
html+="</div>"                  # first child div of angular ends
html+="<div ng-switch-when='bs'>" # second child div of angular
html+="<pre>" + enzdict['BsuMI'] +"</pre>" 
html+="<pre>" +str(res_site['BsuMI']) +"</pre>"    
html+="</div>"                      # second child div of angular ends
html+="<div ng-switch-when='ec'>"   # third child div of angular
html+="<pre>" + enzdict['EcoRI'] +"</pre>" 
html+="<pre>"+str(res_site['EcoRI'])+"</pre>"  
html+="</div>"                      # third child div of angular ends

html+="</div>"   # parent div of angular ends

                   
html+="</div>\n"                    # scroll div ends



html+="</td>"
html+="</tr>"
html+="</table>"
html+="<table>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<p> The coding sequence:</p>\n"
html+="<br>"
html+="<br>"
html+="<br>"
html+="<p> The Peptide Chain: </p>\n"
html+="<br>"
html+="<br>"

html+="</td>"
html+="<td>"
html+="<div class='scroll'>"    # div to scroll

html+="<div id=class='child'>\n" # first child
#html+="<br>"
html+="<pre class='display'>\n"
html+=  coding_sequence 
html+="</pre>\n"                    # first child ends
html+="</div>"
html+="<br>"

html+="<div class='child'>\n" # second child
html+="<pre class='display'>\n"
html+=aligned_amino_acid

html+="</pre>\n"

html+="</div>"              # second child ends

html+="</div>"              # scroll div ends
html+="</td>"
html+="</tr>"
html+="</table>"

html+="<br>"
#******* Create accordian to display codon table ***********. https://www.w3schools.com/howto/howto_js_accordion.asp

html+="<button class='accordion'><p>The Codon Usage Frequency Table : Click to view</p></button>"
html+="<div class='panel'>"
clist=['A','C','G','T']
html+="<div class='container-fluid'>"
html+="<div class='row'>"
html+="<div class='col-sm-6'>"
html+="<p> Gene: Codon Frequency Table </p>"           
html+="<table border='1', style='border-collapse: collapse', id='codon_freq' >"
html+="<tr>"
    
html+="<td></td>"
html+="<th> Codon </th>"
html+="<th> Amino</th>"
html+="<th> Frequency </th>"
html+="<th> Ratio </th>"
html+="</tr>"
freqlist=[]
for c in clist:
    html+="<tr>"
    html+="<td rowspan='65'>" +c+ "</td>"
    
    for key,value in sorted(gene_codon_dict.items()):
        html+="<tr class='high_codon'>"
        if key[0]==c:
           html+="<td>"+key+"</td>"
           html+="<td>"+str(value['aa'])+"</td>"
           html+="<td>"+str(float("{0:.2f}".format(value['freq'])))+"</td>"
           html+="<td>"+str(float("{0:.2f}".format(value['ratio'])))+"</td>"
         
        html+="</tr>"
    html+="</tr>"


html+="</table>" 

html+="</div>"  # columnn
html+="<div class='col-sm-6'>"
html+="<p> Chromosome: Codon Frequency Table </p>"  
html+="<table border='1', style='border-collapse: collapse', id='codon_chrom_freq' >"
html+="<tr>"
    
html+="<td></td>"
html+="<th> Codon </th>"
html+="<th> Amino</th>"
html+="<th> Frequency </th>"
html+="<th> Ratio </th>"
html+="</tr>"

for c in clist:
    html+="<tr>"
    html+="<td rowspan='65'>" +c+ "</td>"
    
    for key,value in sorted(chrom_codon_dict.items()):
        html+="<tr class='high_chrom_codon'>"
        if key[0]==c:
            html+="<td>"+key+"</td>"
            html+="<td>"+str(value['aa'])+"</td>"
            html+="<td>"+str(float("{0:.2f}".format(value['freq'])))+"</td>"
            html+="<td>"+str(float("{0:.2f}".format(value['ratio'])))+"</td>"
        html+="</tr>"     
                
    html+="</tr>"

html+="</table>"

html+="</div>" # column2

html+="</div>" # row
html+="</br>"
html+="<p> Table Keys</p>"
html+="<table id='keys',border='1', style='border-collapse: collapse'>"
html+="<tr>"
html+="<th class='firstcol'> Key </th>"
html+="<th> Meaning</th>"
html+="</tr>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<div class='tablekey overused'></div>"
html+="</td>"
html+="<td>"
html+="<p> Overused Codons </p>"
html+="</td>"
html+="</tr>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<div class='tablekey underused'></div>"
html+="</td>"
html+="<td>"
html+="<p> Underused Codons </p>"
html+="</td>"
html+="</tr>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<p> Frequency</p>"
html+="</td>"
html+="<td>"
html+="<p> Average frequency of this codon per 100 codons </p>"
html+="</td>"
html+="</tr>"
html+="<tr>"
html+="<td class='firstcol'>"
html+="<p> Ratio </p>"
html+="</td>"
html+="<td>"
html+="<p> Abundance of that codon relative to all of the codons for that particular amino acid </p>"
html+="</td>"
html+="</tr>"
html+="</table>"
html+="</div>" # conainer



html+="</div>" # panel
html+="</div>" # wrapper



html+="<footer class='footer'>"
html+="<p>Group : 1 Chromosome: 18 </p>"
html+="<script type='text/javascript' src='/frontend/src/html/js/lastmodified.js'></script>\n"
html+="<script type='text/javascript' src='/frontend/WWW/js/email.js'></script>\n"


html+=" </footer>"
html+="<script type='text/javascript' src='/frontend/src/html/js/jquery.js'></script>\n"
html+="<script type='text/javascript' src='/frontend/src/html/js/biocw.js'></script>\n"

html+="</body>\n"

html+="</html>\n"

print(html)
		
